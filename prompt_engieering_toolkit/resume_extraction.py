import json
import os
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from pydantic import BaseModel, Field, ValidationError

PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(PROJECT_ROOT / ".env")

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file.")

client = genai.Client(api_key=api_key)
MODEL_NAME = "gemini-3.5-flash-lite"


class ResumeData(BaseModel):
    name: str = Field(min_length=1)
    skills: list[str]
    years_experience: float = Field(ge=0)


DATA_FILE = Path(__file__).parent / "resume_golden_set.json"

with open(DATA_FILE, "r", encoding="utf-8") as file:
    resumes = json.load(file)


def extract_resume(resume_text, use_json_mode):
    prompt = f"""
Extract information from the resume below.

Return these fields:
- name: candidate name
- skills: list of technical skills
- years_experience: number of years of professional experience

If information is missing, use an empty string for name,
an empty list for skills, and 0 for years_experience.
Do not invent information.

Resume:
{resume_text}
"""

    config = {"temperature": 0}

    if use_json_mode:
        config["response_mime_type"] = "application/json"

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
        config=config
    )

    return response.text


if __name__== "__main__":
    results = []

    for item in resumes:
        print(f"\nTesting resume {item['id']}...")

        for use_json_mode in [False, True]:
            mode = "JSON mode" if use_json_mode else "Plain prompt"

            try:
                raw_output = extract_resume(item["resume"], use_json_mode)
                parsed_json = json.loads(raw_output)
                validated = ResumeData.model_validate(parsed_json)

                result = {
                    "resume_id": item["id"],
                    "mode": mode,
                    "valid_json": True,
                    "validated_data": validated.model_dump(),
                    "expected": item["expected"]
                }

                print(f"{mode}: Valid JSON and schema")

            except (json.JSONDecodeError, ValidationError) as error:
                result = {
                    "resume_id": item["id"],
                    "mode": mode,
                    "valid_json": False,
                    "error": str(error)
                }

                print(f"{mode}: Invalid output - {error}")

            except Exception as error:
                result = {
                    "resume_id": item["id"],
                    "mode": mode,
                    "error": str(error)
                }

                print(f"{mode}: API or other error - {error}")

            results.append(result)

    output_file = Path(__file__).parent / "resume_extraction_results.json"

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(results, file, indent=2, ensure_ascii=False)

    print(f"\nResults saved to: {output_file}")
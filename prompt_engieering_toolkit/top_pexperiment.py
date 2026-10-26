import json
import os
from pathlib import Path
from google import genai
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(PROJECT_ROOT / ".env")

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file.")

client = genai.Client(api_key=api_key)
MODEL_NAME = "gemini-3.5-flash-lite"

prompt = """
Write a creative 5-sentence story about a robot
that discovers a hidden garden on the Moon.
"""

top_p_values = [0.3, 0.95]
results = []

for top_p in top_p_values:
    print(f"\nTesting top_p = {top_p}")

    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt,
            config={
                "temperature": 0.7,
                "top_p": top_p
            }
        )

        story = response.text or ""
        print(story)

        results.append({
            "top_p": top_p,
            "temperature": 0.7,
            "prompt": prompt,
            "response": story
        })

    except Exception as error:
        print(f"Error at top_p={top_p}: {error}")

output_file = Path(__file__).parent / "top_p_results.json"

with open(output_file, "w", encoding="utf-8") as file:
    json.dump(results, file, indent=2, ensure_ascii=False)

print(f"\nResults saved to: {output_file}")
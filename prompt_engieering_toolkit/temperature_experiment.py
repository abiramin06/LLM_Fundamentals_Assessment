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
Write a short, creative story in 5 sentences about a robot
that learns to paint. Make the story interesting and imaginative.
"""

temperatures = [0, 0.7, 1.2]
results = []

for temperature in temperatures:
    print(f"\nTesting temperature: {temperature}")

    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt,
            config={
                "temperature": temperature
            }
        )

        story = response.text or ""

        print("Generated story:")
        print(story)

        results.append({
            "temperature": temperature,
            "prompt": prompt,
            "response": story
        })

    except Exception as error:
        print(f"Error at temperature {temperature}: {error}")

output_file = Path(__file__).parent / "temperature_results.json"

with open(output_file, "w", encoding="utf-8") as file:
    json.dump(results, file, indent=2, ensure_ascii=False)

print(f"\nResults saved to: {output_file}")
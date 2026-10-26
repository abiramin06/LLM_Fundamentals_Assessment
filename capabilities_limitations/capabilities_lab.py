import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

client = genai.Client(api_key=api_key)

tasks = [
    {
        "name": "Summarization",
        "prompt": (
            "Summarize this text in 2 sentences:\n"
            "AI helps businesses automate tasks, analyze data, improve "
            "customer service, and make predictions. However, AI can make "
            "mistakes, so important results should be checked by humans."
        ),
    },
    {
        "name": "Classification",
        "prompt": (
            "Classify this customer message as Billing, Technical, or Account. "
            "Return only the category.\n"
            "Message: I was charged twice for my subscription."
        ),
    },
    {
        "name": "Information Extraction",
        "prompt": (
            "Extract the name, skills, and years of experience from this text. "
            "Return valid JSON with keys name, skills, years_of_experience.\n"
            "Text: Priya knows Python and SQL and has 2 years of experience."
        ),
    },
    {
        "name": "Translation",
        "prompt": (
            "Translate this Tamil sentence into English:\n"
            "வணக்கம், நீங்கள் எப்படி இருக்கிறீர்கள்?"
        ),
    },
    {
        "name": "Code Generation",
        "prompt": (
            "Write a Python function named add_numbers that accepts two "
            "numbers and returns their sum. Include a short example."
        ),
    },
]

results = []

for task in tasks:
    print("\n" + "=" * 50)
    print("TASK:", task["name"])
    print("PROMPT:", task["prompt"])

    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=task["prompt"],
        )

        answer = response.text or "[No text returned]"
        print("ANSWER:", answer)

        rating = int(input("Rate this answer from 1 to 5: "))
        rating = max(1, min(5, rating))

        results.append({
            "task": task["name"],
            "prompt": task["prompt"],
            "answer": answer,
            "rating": rating,
        })

    except Exception as error:
        print("ERROR:", error)
        results.append({
            "task": task["name"],
            "prompt": task["prompt"],
            "answer": f"API request failed: {error}",
            "rating": 0,
        })

with open("capabilities_limitations/capabilities_results.json",
          "w", encoding="utf-8") as file:
    json.dump(results, file, indent=2, ensure_ascii=False)

print("\nResults saved to capabilities_limitations/capabilities_results.json")
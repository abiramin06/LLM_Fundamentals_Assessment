import json
import os
from pathlib import Path
from google import genai
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(PROJECT_ROOT / ".env")

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in the project root .env file.")

client = genai.Client(api_key=api_key)
MODEL_NAME = "gemini-3.5-flash-lite"

problems = [
    {
        "question": "A notebook costs Rs. 50. What is the total cost of 3 notebooks?",
        "answer": "150"
    },
    {
        "question": "Five workers each complete 10 tasks. How many tasks do they complete altogether?",
        "answer": "50"
    },
    {
        "question": "Find the next number: 2, 4, 8, 16, __.",
        "answer": "32"
    },
    {
        "question": "All roses are flowers. Some flowers fade quickly. Can we conclude that all roses fade quickly? Answer Yes or No.",
        "answer": "No"
    },
    {
        "question": "A bat and a ball cost Rs. 110 together. The bat costs Rs. 100 more than the ball. How much does the ball cost in rupees?",
        "answer": "5"
    }
]


def ask_model(question, step_by_step):
    if step_by_step:
        instruction = (
            "Solve the problem carefully. Check your calculations, "
            "then give the final answer. Briefly explain the key steps."
        )
    else:
        instruction = "Give only the final answer."

    prompt = f"""
{instruction}

Problem: {question}

Return JSON only in this format:
{{"answer": "your final answer"}}
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
        config={
            "temperature": 0,
            "response_mime_type": "application/json"
        }
    )

    return json.loads(response.text)


if __name__ == "__main__":
    results = []

    for index, problem in enumerate(problems, start=1):
        print(f"\nProblem {index}: {problem['question']}")

        for step_by_step in [False, True]:
            label = "Step-by-step prompt" if step_by_step else "Direct prompt"

            try:
                prediction = ask_model(problem["question"], step_by_step)
                answer = str(prediction.get("answer", "")).strip()

                print(f"{label}: {answer}")

                results.append({
                    "problem_number": index,
                    "question": problem["question"],
                    "prompt_type": label,
                    "expected_answer": problem["answer"],
                    "predicted_answer": answer
                })

            except Exception as error:
                print(f"{label} error: {error}")

    output_file = Path(__file__).parent / "reasoning_results.json"

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(results, file, indent=2, ensure_ascii=False)

    print(f"\nResults saved to: {output_file}")
import json
from pathlib import Path
from google import genai
from dotenv import load_dotenv
import os

PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(PROJECT_ROOT / ".env")

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY not found. Check the .env file in your project root."
    )

client = genai.Client(api_key=api_key)

MODEL_NAME = "gemini-3.5-flash-lite"

DATA_FILE = Path(__file__).parent / "golden_set.json"

with open(DATA_FILE, "r", encoding="utf-8") as file:
    tickets = json.load(file)


def classify_ticket(ticket_text, prompt_version):
    if prompt_version == 1:
        prompt = f"""
Classify this support ticket.

Ticket: {ticket_text}

Choose one category: Billing, Technical, Account.
Choose one priority: High, Medium, Low.

Return only JSON:
{{"category": "...", "priority": "..."}}
"""

    elif prompt_version == 2:
        prompt = f"""
Role:
You are a customer support ticket classification assistant.

Task:
Classify the ticket into one category and one priority.

Constraints:
- Category must be Billing, Technical, or Account.
- Priority must be High, Medium, or Low.
- High: urgent payment problems, account lockouts, or major outages.
- Medium: functionality problems or issues needing attention.
- Low: general questions or routine changes.
- Do not add explanations or extra fields.

Output format:
Return valid JSON only:
{{"category": "...", "priority": "..."}}

Ticket:
{ticket_text}
"""

    else:
        prompt = f"""
Role:
You classify customer support tickets.

Task:
Return the category and priority as JSON.

Examples:

Ticket: I was charged twice for my subscription.
Output: {{"category": "Billing", "priority": "High"}}

Ticket: How can I download my invoice?
Output: {{"category": "Billing", "priority": "Low"}}

Ticket: My account is locked after several login attempts.
Output: {{"category": "Account", "priority": "High"}}

Now classify this ticket.

Ticket: {ticket_text}

Allowed categories: Billing, Technical, Account.
Allowed priorities: High, Medium, Low.

Return only valid JSON with keys category and priority.
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


def evaluate_prompt(prompt_version):
    correct = 0
    results = []

    for item in tickets:
        try:
            prediction = classify_ticket(item["ticket"], prompt_version)

            category_correct = (
                prediction.get("category") == item["expected_category"]
            )
            priority_correct = (
                prediction.get("priority") == item["expected_priority"]
            )

            is_correct = category_correct and priority_correct

            if is_correct:
                correct += 1

            results.append({
                "id": item["id"],
                "ticket": item["ticket"],
                "expected_category": item["expected_category"],
                "predicted_category": prediction.get("category"),
                "expected_priority": item["expected_priority"],
                "predicted_priority": prediction.get("priority"),
                "correct": is_correct
            })

        except Exception as error:
            results.append({
                "id": item["id"],
                "ticket": item["ticket"],
                "correct": False,
                "error": str(error)
            })

    accuracy = (correct / len(tickets)) * 100

    return {
        "prompt_version": prompt_version,
        "correct": correct,
        "total": len(tickets),
        "accuracy_percent": round(accuracy, 2),
        "results": results
    }


if __name__ == "__main__":
    all_results = []
    
for version in [1, 2, 3]:
        print(f"\nTesting Prompt Version {version}...")
        result = evaluate_prompt(version)

        print(
            f"Accuracy: {result['correct']}/{result['total']} "
            f"({result['accuracy_percent']}%)"
        )

        all_results.append(result)

output_file = Path(__file__).parent / "classification_results.json"

with open(output_file, "w", encoding="utf-8") as file:
    json.dump(all_results, file, indent=2, ensure_ascii=False)

print(f"\nResults saved to: {output_file}")

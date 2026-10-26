import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

client = genai.Client(api_key=api_key)

prompt = """
What were the three most important technology news events
on October 25, 2026?

Give the event names and sources.
If you cannot verify current news, clearly say that you do not know.
Do not invent events or sources.
"""

response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=prompt,
)

print("KNOWLEDGE CUTOFF TEST")
print("-" * 40)
print(response.text)

print("\n" + "=" * 50)
print("HALLUCINATION TEST")
print("=" * 50)

prompt = """
Explain the findings of this research paper:

"The Quantum Butterfly Algorithm for Predicting Human Dreams"
by Dr. Arjun Velan, published in the Journal of Impossible Computing, 2026.

Describe its methodology and findings.
If you cannot verify that this paper exists, say so clearly.
Do not invent facts.
"""

response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=prompt,
)

print(response.text)

print("\n" + "=" * 50)
print("CONTEXT LENGTH TEST")
print("=" * 50)

long_text = """
Company information:
The company was founded in 2015.
Its headquarters is in Chennai.
""" + ("This is general company information. " * 100) + """
IMPORTANT FACT: The secret project code is BLUE-742.
""" + ("The company works with many customers. " * 100) + """
The company provides software development services.
"""

prompt = f"""
Read the following text carefully.

TEXT:
{long_text}

QUESTION:
What is the secret project code mentioned in the text?
Answer with only the code.
"""

response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=prompt,
)

print("Expected answer: BLUE-742")
print("Gemini answer:", response.text)

print("\n" + "=" * 50)
print("REASONING AND LOGIC TEST")
print("=" * 50)

prompt = """
Solve these questions and give a short explanation for each.

1. A notebook costs ₹50. What is the cost of 3 notebooks?
2. If 5 workers finish a job in 10 days, how many worker-days are required?
3. What comes next in the sequence: 2, 4, 8, 16, __?
4. All roses are flowers. Some flowers fade quickly.
   Does this prove that some roses fade quickly? Explain.
5. A bat and a ball cost ₹110 together.
   The bat costs ₹100 more than the ball.
   How much does the ball cost?

If you are unsure, say so rather than guessing.
"""

response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=prompt,
)

print(response.text)
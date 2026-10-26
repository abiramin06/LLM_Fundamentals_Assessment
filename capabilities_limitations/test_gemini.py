import os
from dotenv import load_dotenv
from google import genai

# Load environment variables from the project root .env file
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("ERROR: Gemini API key not found in .env")
else:
    try:
        client = genai.Client(api_key=api_key)

        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents="Reply with only this text: Gemini API connection successful!"
        )

        print("SUCCESS: Gemini API connection working!")
        print("Response:", response.text)

    except Exception as e:
        print("API request failed:", e)
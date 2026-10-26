import tiktoken

encoding = tiktoken.get_encoding("cl100k_base")

texts = {
    "Sentence": "Artificial intelligence helps businesses.",

    "Paragraph": (
        "Large language models can understand and generate text. "
        "They are useful for summarization, translation, and classification."
    ),

    "Page": (
        "Artificial intelligence is transforming modern businesses. "
        "Machine learning identifies patterns in data. "
        "Deep learning uses neural networks to learn complex patterns. "
        "Large language models can generate text and answer questions. "
        "They can summarize documents and extract useful information. "
        "However, they may sometimes produce incorrect information. "
        "Businesses should validate important outputs. "
        "They should also consider privacy, cost, and response time."
    ),

    "JSON": (
        '{"name": "Priya", "skills": ["Python", "SQL"], '
        '"experience": 2, "role": "Data Scientist"}'
    ),

    "Tamil": "வணக்கம், நீங்கள் எப்படி இருக்கிறீர்கள்?"
}

print("-" * 65)
print(f"{'Text Type':<15}{'Words':<10}{'Tokens':<10}{'Words/Token':<15}")
print("-" * 65)

for text_type, text in texts.items():

    words = len(text.split())

    tokens = len(encoding.encode(text))

    words_per_token = words / tokens if tokens else 0

    print(
        f"{text_type:<15}"
        f"{words:<10}"
        f"{tokens:<10}"
        f"{words_per_token:<15.3f}"
    )

    print("Fits in 8K context:", tokens <= 8192)
    print("Fits in 128K context:", tokens <= 128000)
    print()
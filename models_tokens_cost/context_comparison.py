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
        "Businesses should validate important outputs."
    ),
    "JSON": '{"name": "Priya", "skills": ["Python", "SQL"], "experience": 2}',
    "Tamil": "வணக்கம், நீங்கள் எப்படி இருக்கிறீர்கள்?"
}

for name, text in texts.items():
    tokens = len(encoding.encode(text))

    print(f"\n{name}")
    print("Token count:", tokens)
    print("Fits in 8K context:", tokens <= 8192)
    print("Fits in 128K context:", tokens <= 128000)
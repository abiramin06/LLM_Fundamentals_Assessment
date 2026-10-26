from transformers import pipeline

print("=" * 50)
print("BERT FILL-MASK TASK")
print("=" * 50)

fill_mask = pipeline(
    "fill-mask",
    model="google-bert/bert-base-uncased"
)

result = fill_mask("Artificial intelligence is [MASK].")

for item in result[:3]:
    print(item["sequence"], "Score:", round(item["score"], 4))


print("\n" + "=" * 50)
print("GPT-2 TEXT GENERATION")
print("=" * 50)

generator = pipeline(
    "text-generation",
    model="openai-community/gpt2"
)

result = generator(
    "Artificial intelligence will",
    max_new_tokens=30,
    num_return_sequences=1,
    do_sample=False,
    pad_token_id=generator.tokenizer.eos_token_id
)

print(result[0]["generated_text"])
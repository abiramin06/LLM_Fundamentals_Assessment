Prompt Engineering Toolkit: Bad Prompts and Improvements

Prompt 1: Summarization

Bad Prompt:
Summarize this.

Problems:

- The required summary length is not specified.
- The target audience is unclear.
- Important information to preserve is not mentioned.

Improved Prompt:
You are a summarization assistant. Summarize the provided text in 5 bullet points using simple English. Preserve the main ideas, important facts, and conclusions. Do not introduce information that is not present in the original text.

Prompt 2: Customer Support Classification

Bad Prompt:
Check this ticket.

Problems:

- The task is unclear.
- The allowed categories are not specified.
- The expected output format is missing.

Improved Prompt:
You are a customer support classification assistant. Classify the given ticket into exactly one category: Billing, Technical, or Account. Assign one priority: High, Medium, or Low. Return valid JSON with the keys "category" and "priority". Do not include explanations or additional fields.

Prompt 3: Resume Information Extraction

Bad Prompt:
Tell me about this resume.

Problems:

- The information to extract is not specified.
- There are no instructions for missing information.
- A structured output format is not provided.

Improved Prompt:
You are a resume information extraction assistant. Extract the candidate's name, technical skills, and years of professional experience from the provided resume. Return valid JSON with the fields "name", "skills", and "years_experience". Use an empty string for a missing name, an empty list for missing skills, and 0 when years of experience are not stated. Do not invent information.

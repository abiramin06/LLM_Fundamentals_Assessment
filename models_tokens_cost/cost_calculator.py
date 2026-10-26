def estimate_cost(input_tokens, output_tokens, price_in, price_out):
    """
    Estimate LLM API cost.

    Prices are given per 1 million tokens.
    """
    input_cost = (input_tokens / 1_000_000) * price_in
    output_cost = (output_tokens / 1_000_000) * price_out

    total_cost = input_cost + output_cost

    return total_cost


chats_per_day = 1000
days_per_month = 30

input_tokens_per_chat = 1500
output_tokens_per_chat = 400

monthly_input_tokens = (
    chats_per_day * days_per_month * input_tokens_per_chat
)

monthly_output_tokens = (
    chats_per_day * days_per_month * output_tokens_per_chat
)

price_in = 1.00
price_out = 4.00

monthly_cost = estimate_cost(
    monthly_input_tokens,
    monthly_output_tokens,
    price_in,
    price_out
)

print("MONTHLY LLM API COST ESTIMATION")
print("-" * 35)
print("Chats per day:", chats_per_day)
print("Monthly input tokens:", monthly_input_tokens)
print("Monthly output tokens:", monthly_output_tokens)
print("Input price per million tokens: $", price_in)
print("Output price per million tokens: $", price_out)
print(f"Estimated monthly cost: ${monthly_cost:.2f}")
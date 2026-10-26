Transformer Architecture: Key Concepts

1. Encoder-only models: Models such as BERT use encoder layers to understand context and are useful for classification, sentiment analysis, and masked-word prediction.

2. Decoder-only models: Models such as GPT-2 use decoder layers with causal attention to predict the next token and generate text.

3. Self-attention: It calculates relationships between tokens using Query (Q), Key (K), and Value (V) representations.

4. Multi-head attention: It uses multiple attention heads to learn different relationships between tokens and combines their outputs.

5. Positional encoding: It adds information about token positions because attention alone does not inherently represent token order.

6. Why Transformers replaced many RNN-based approaches: Transformers can process tokens in parallel during training and capture long-range relationships more effectively in many tasks. However, RNNs are still useful in some applications.
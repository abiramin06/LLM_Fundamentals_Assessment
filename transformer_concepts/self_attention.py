import numpy as np

Q = np.array([
    [1, 0],
    [0, 1],
    [1, 1],
    [0.5, 0.5]
], dtype=float)

K = np.array([
    [1, 0],
    [0, 1],
    [1, 1],
    [0.5, 0.5]
], dtype=float)

V = np.array([
    [10, 0],
    [0, 10],
    [10, 10],
    [5, 5]
], dtype=float)


d_k = K.shape[1]
scores = Q @ K.T / np.sqrt(d_k)

scores_shifted = scores - np.max(scores, axis=1, keepdims=True)
exp_scores = np.exp(scores_shifted)
attention_weights = exp_scores / np.sum(
    exp_scores, axis=1, keepdims=True
)

output = attention_weights @ V

print("Attention Weights (4x4):")
print(np.round(attention_weights, 3))

print("\nRow sums (should all be 1):")
print(np.round(attention_weights.sum(axis=1), 3))

print("\nSelf-Attention Output:")
print(np.round(output, 3))
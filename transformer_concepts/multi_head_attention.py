import numpy as np

X = np.array([
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 1, 0, 0],
    [0, 0, 1, 1]
], dtype=float)

def attention(Q, K, V):
    d_k = K.shape[1]

    scores = Q @ K.T / np.sqrt(d_k)

    # Softmax
    scores = scores - np.max(scores, axis=1, keepdims=True)
    weights = np.exp(scores)
    weights = weights / np.sum(weights, axis=1, keepdims=True)

    output = weights @ V
    return output, weights


WQ1 = np.array([[1, 0], [0, 1], [1, 0], [0, 1]], dtype=float)
WK1 = WQ1.copy()
WV1 = WQ1.copy()

WQ2 = np.array([[0, 1], [1, 0], [0, 1], [1, 0]], dtype=float)
WK2 = WQ2.copy()
WV2 = WQ2.copy()

Q1, K1, V1 = X @ WQ1, X @ WK1, X @ WV1
Q2, K2, V2 = X @ WQ2, X @ WK2, X @ WV2

head1, weights1 = attention(Q1, K1, V1)
head2, weights2 = attention(Q2, K2, V2)

combined = np.concatenate([head1, head2], axis=1)

W_O = np.eye(4)
final_output = combined @ W_O

print("Head 1 output:")
print(np.round(head1, 3))

print("\nHead 2 output:")
print(np.round(head2, 3))

print("\nConcatenated output shape:", combined.shape)
print("\nFinal output:")
print(np.round(final_output, 3))
print("\nFinal output shape:", final_output.shape)
import numpy as np
import matplotlib.pyplot as plt

sequence_length = 10
d_model = 8

pos = np.arange(sequence_length)[:, np.newaxis]
i = np.arange(d_model)[np.newaxis, :]

angle_rates = 1 / np.power(
    10000, (2 * (i // 2)) / d_model
)

angles = pos * angle_rates

encoding = np.zeros((sequence_length, d_model))
encoding[:, 0::2] = np.sin(angles[:, 0::2])
encoding[:, 1::2] = np.cos(angles[:, 1::2])

print("Positional Encoding Matrix (10 x 8):")
print(np.round(encoding, 3))

print("\nMatrix shape:", encoding.shape)

plt.figure(figsize=(10, 6))
plt.imshow(encoding, aspect="auto")
plt.colorbar(label="Encoding Value")
plt.xlabel("Embedding Dimension")
plt.ylabel("Position")
plt.title("Sinusoidal Positional Encoding")
plt.xticks(range(d_model))
plt.yticks(range(sequence_length))
plt.tight_layout()
plt.savefig("transformer_concepts/positional_encoding.png")
plt.show()


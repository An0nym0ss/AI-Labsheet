w1, w2, bias = 0.0, 0.0, 0.0
lr = 0.1
epoch = 0

and_data = [
    [0, 0, 0],
    [0, 1, 0],
    [1, 0, 0],
    [1, 1, 1]
]

print("AND Logic Gate Training Data:")
for row in and_data:
    print("\t".join(map(str, row)))

print("\nTraining started...\n")

while epoch < 100:
    error_count = 0

    for x1, x2, t in and_data:
        z = w1 * x1 + w2 * x2 + bias
        o = 1 if z >= 0 else 0

        if t != o:
            w1 += lr * (t - o) * x1
            w2 += lr * (t - o) * x2
            bias += lr * (t - o)
            error_count += 1

    print(f"Epoch {epoch + 1}: w1={w1:.2f}, w2={w2:.2f}, bias={bias:.2f}")

    if error_count == 0:
        print("Training converged.")
        break

    epoch += 1

print("\nFinal weights and bias after training:")
print(f"w1 = {w1:.2f}")
print(f"w2 = {w2:.2f}")
print(f"bias = {bias:.2f}")
print("\nTesting the trained Perceptron:")
for x1, x2, t in and_data:
    z = w1 * x1 + w2 * x2 + bias
    o = 1 if z >= 0 else 0
    print(f"Input: {x1} {x2} => Output: {o} (Expected: {t})")
def train_perceptron(data, gate_name):
    w1, w2, bias = 0.0, 0.0, 0.0
    lr = 0.1
    epoch = 0

    print(f"{gate_name} Logic Gate Training Data:")
    for row in data:
        print("\t".join(map(str, row)))

    print(f"\n{gate_name} Training started...\n")

    while epoch < 100:
        error_count = 0

        for x1, x2, t in data:
            z = w1 * x1 + w2 * x2 + bias
            o = 1 if z >= 0 else 0

            if t != o:
                w1 += lr * (t - o) * x1
                w2 += lr * (t - o) * x2
                bias += lr * (t - o)
                error_count += 1

        print(f"Epoch {epoch + 1}: w1={w1:.2f}, w2={w2:.2f}, bias={bias:.2f}")

        if error_count == 0:
            print(f"{gate_name} Training converged.")
            break

        epoch += 1

    print(f"\nFinal weights and bias after {gate_name} training:")
    print(f"w1 = {w1:.2f}")
    print(f"w2 = {w2:.2f}")
    print(f"bias = {bias:.2f}")
    print(f"\nTesting the trained {gate_name} Perceptron:")
    
    correct = 0
    for x1, x2, t in data:
        z = w1 * x1 + w2 * x2 + bias
        o = 1 if z >= 0 else 0
        status = "✓" if o == t else "✗"
        print(f"Input: {x1} {x2} => Output: {o} (Expected: {t}) {status}")
        if o == t:
            correct += 1
    
    accuracy = (correct / len(data)) * 100
    print(f"Accuracy: {accuracy:.1f}%")
    return w1, w2, bias

# Training data
and_data = [
    [0, 0, 0],
    [0, 1, 0],
    [1, 0, 0],
    [1, 1, 1]
]

or_data = [
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

# Train AND gate
print("=" * 50)
print("TRAINING AND GATE")
print("=" * 50)
and_w1, and_w2, and_bias = train_perceptron(and_data, "AND")

# Train OR gate
print("\n" + "=" * 50)
print("TRAINING OR GATE")
print("=" * 50)
or_w1, or_w2, or_bias = train_perceptron(or_data, "OR")

# Summary
print("\n" + "=" * 50)
print("SUMMARY")
print("=" * 50)
print(f"AND Gate - Final weights: w1={and_w1:.2f}, w2={and_w2:.2f}, bias={and_bias:.2f}")
print(f"OR Gate  - Final weights: w1={or_w1:.2f}, w2={or_w2:.2f}, bias={or_bias:.2f}")
import random

# Generate random dataset for the linear function y = 2x₁ + 3x₂ - x₃ + 5
def generate_dataset(num_samples=10):
    inputs = []
    targets = []
    
    print("Generated Dataset:")
    print("x₁\t x₂\t x₃\t -> y")
    print("-" * 30)
    
    for i in range(num_samples):
        x1 = random.uniform(0, 1)
        x2 = random.uniform(0, 1)
        x3 = random.uniform(0, 1)
        
        # True function: y = 2x₁ + 3x₂ - x3 + 5
        y = 2*x1 + 3*x2 - x3 + 5
        
        inputs.append([x1, x2, x3])
        targets.append(y)
        
        print(f"{x1:.3f}\t {x2:.3f}\t {x3:.3f}\t -> {y:.3f}")
    
    return inputs, targets

# Generate training data
inputs, targets = generate_dataset(10)

# Initialize weights and bias for 3 inputs
weights = [0, 0, 0]
bias = 0
learning_rate = 0.01

print(f"\nInitial weights: {weights}, bias: {bias}")
print(f"Target function: y = 2x₁ + 3x₂ - x₃ + 5")
print(f"Learning rate: {learning_rate}")
print("\nTraining Progress:")
print("-" * 50)

for epoch in range(100):
    total_squared_error = 0
    
    for i, x in enumerate(inputs):
        # Linear activation: output = weighted sum + bias
        output = weights[0]*x[0] + weights[1]*x[1] + weights[2]*x[2] + bias
        error = targets[i] - output
        squared_error = error ** 2
        total_squared_error += squared_error
        
        # Update weights and bias using gradient descent
        weights[0] += learning_rate * error * x[0]
        weights[1] += learning_rate * error * x[1]
        weights[2] += learning_rate * error * x[2]
        bias += learning_rate * error
    
    # Calculate Mean Squared Error
    mse = total_squared_error / len(inputs)
    
    # Display progress every 10 epochs
    if epoch % 10 == 0 or epoch == 99:
        print(f"Epoch {epoch:2d}: MSE = {mse:.6f}, Weights = [{weights[0]:.3f}, {weights[1]:.3f}, {weights[2]:.3f}], Bias = {bias:.3f}")
    
    # Check for convergence
    if mse < 0.0001:
        print(f"Converged at epoch {epoch}!")
        break

print("\n" + "=" * 60)
print("FINAL RESULTS")
print("=" * 60)
print(f"Target function:  y = 2x₁ + 3x₂ - x₃ + 5")
print(f"Learned function: y = {weights[0]:.3f}x₁ + {weights[1]:.3f}x₂ + {weights[2]:.3f}x₃ + {bias:.3f}")
print(f"Final MSE: {mse:.6f}")

# Testing on the training data
print("\nTesting on Training Data:")
print("Input (x₁, x₂, x₃)\t\tPredicted\tActual\t\tError")
print("-" * 65)

total_test_error = 0
for i, x in enumerate(inputs):
    predicted = weights[0]*x[0] + weights[1]*x[1] + weights[2]*x[2] + bias
    actual = targets[i]
    error = abs(predicted - actual)
    total_test_error += error
    
    print(f"({x[0]:.3f}, {x[1]:.3f}, {x[2]:.3f})\t\t{predicted:.3f}\t\t{actual:.3f}\t\t{error:.3f}")

print(f"\nMean Absolute Error: {total_test_error / len(inputs):.6f}")
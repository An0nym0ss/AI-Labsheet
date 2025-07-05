import random

def generate_dataset(n_features, n_samples=10):
    random.seed(42)
    X = []
    for i in range(n_samples):
        row = [random.uniform(0, 1) for _ in range(n_features)]
        X.append(row)
    
    true_weights = [random.uniform(-1, 1) for _ in range(n_features)]
    bias = 5
    
    y = []
    for i in range(n_samples):
        y_val = sum(X[i][j] * true_weights[j] for j in range(n_features)) + bias
        y.append(y_val)
    
    return X, y, true_weights, bias

def train_perceptron(X, y, learning_rate=0.01, epochs=100):
    n_samples = len(X)
    n_features = len(X[0])
    weights = [random.uniform(-0.5, 0.5) for _ in range(n_features)]
    bias = random.uniform(-0.5, 0.5)
    
    print(f"Initial weights: {[f'{w:.3f}' for w in weights]}")
    print(f"Initial bias: {bias:.3f}")
    print("-" * 50)
    
    for epoch in range(1, epochs + 1):
        total_error = 0
        for i in range(n_samples):
            x_i = X[i]
            y_pred = sum(weights[j] * x_i[j] for j in range(n_features)) + bias
            error = y[i] - y_pred
            total_error += error ** 2

            for j in range(n_features):
                weights[j] += learning_rate * error * x_i[j]
            bias += learning_rate * error
        
        mse = total_error / n_samples
        if epoch % 10 == 0 or epoch == epochs:
            print(f"Epoch {epoch:3d} | MSE: {mse:.6f} | Weights: {[f'{w:.3f}' for w in weights]} | Bias: {bias:.3f}")
        
        if mse < 0.001:
            print(f"Converged at epoch {epoch}!")
            break
    
    return weights, bias

def run_test(n_features):
    print(f"\n{'='*60}")
    print(f"TRAINING PERCEPTRON WITH {n_features} FEATURES")
    print(f"{'='*60}")
    
    X, y, true_w, true_b = generate_dataset(n_features)
    
    print(f"True weights: {[f'{w:.3f}' for w in true_w]}")
    print(f"True bias: {true_b:.3f}")
    print(f"Dataset size: {len(X)} samples")
    
    weights, bias = train_perceptron(X, y)
    
    print(f"\nFinal Results:")
    print(f"Learned Weights: {[f'{w:.3f}' for w in weights]}")
    print(f"Learned Bias: {bias:.3f}")
    
    print(f"\nTesting on training data:")
    total_mae = 0
    for i in range(len(X)):
        predicted = sum(weights[j] * X[i][j] for j in range(n_features)) + bias
        actual = y[i]
        error = abs(predicted - actual)
        total_mae += error
        print(f"Sample {i+1}: Predicted={predicted:.3f}, Actual={actual:.3f}, Error={error:.3f}")
    
    mae = total_mae / len(X)
    print(f"Mean Absolute Error: {mae:.6f}")

def main():
    print("LINEAR REGRESSION USING PERCEPTRON")
    run_test(n_features=4)
    run_test(n_features=5)

if __name__ == "__main__":
    main()
import itertools

def step_function(x):
    return 1 if x >= 0 else 0

def generate_truth_table(n_inputs, gate_type):
    truth_table = []
    for input_combination in itertools.product([0, 1], repeat=n_inputs):
        if gate_type.upper() == "AND":
            output = 1 if all(input_combination) else 0
        elif gate_type.upper() == "OR":
            output = 1 if any(input_combination) else 0
        else:
            raise ValueError("Gate type must be 'AND' or 'OR'")
        truth_table.append((list(input_combination), output))
    return truth_table

def display_truth_table(truth_table, n_inputs, gate_type):
    print(f"\nTruth Table for {gate_type} Gate ({n_inputs} inputs):")
    header = " ".join([f"x{i+1}" for i in range(n_inputs)]) + " | y"
    print(header)
    print("-" * len(header))
    
    for inputs, output in truth_table:
        input_str = " ".join([f" {x}" for x in inputs])
        print(f"{input_str} | {output}")

def train_perceptron(n_inputs, gate_type, learning_rate=0.1, max_epochs=100):
    truth_table = generate_truth_table(n_inputs, gate_type)
    weights = [0.0] * n_inputs
    bias = 0.0
    
    print(f"\n{'='*60}")
    print(f"TRAINING {gate_type} GATE WITH {n_inputs} INPUTS")
    print(f"{'='*60}")
    
    display_truth_table(truth_table, n_inputs, gate_type)
    
    print(f"\nInitial Parameters:")
    print(f"Weights: {weights}")
    print(f"Bias: {bias}")
    print(f"Learning Rate: {learning_rate}")
    
    print(f"\nTraining Progress:")
    print("-" * 50)
    
    for epoch in range(max_epochs):
        total_errors = 0
        
        for inputs, target in truth_table:
            weighted_sum = sum(w * x for w, x in zip(weights, inputs)) + bias
            predicted = step_function(weighted_sum)
            error = target - predicted
            
            if error != 0:
                total_errors += 1
                for i in range(n_inputs):
                    weights[i] += learning_rate * error * inputs[i]
                bias += learning_rate * error
        
        if epoch % 10 == 0 or epoch == max_epochs - 1:
            print(f"Epoch {epoch+1:2d}: Weights={[f'{w:.2f}' for w in weights]}, Bias={bias:.2f}, Errors={total_errors}")
        
        if total_errors == 0:
            print(f"Converged after {epoch+1} epochs!")
            break
    
    print(f"\nTesting Results:")
    print("-" * 50)
    header = " ".join([f"x{i+1}" for i in range(n_inputs)]) + " | Predicted | Expected | Status"
    print(header)
    print("-" * len(header))
    
    correct_predictions = 0
    for inputs, expected in truth_table:
        weighted_sum = sum(w * x for w, x in zip(weights, inputs)) + bias
        predicted = step_function(weighted_sum)
        status = "PASS" if predicted == expected else "FAIL"
        correct_predictions += (predicted == expected)
        
        input_str = " ".join([f" {x}" for x in inputs])
        print(f"{input_str} |    {predicted}      |    {expected}     |  {status}")
    
    accuracy = (correct_predictions / len(truth_table)) * 100
    
    print(f"\nFinal Results:")
    print(f"Final Weights: {[f'{w:.3f}' for w in weights]}")
    print(f"Final Bias: {bias:.3f}")
    print(f"Training Epochs: {epoch+1}")
    print(f"Accuracy: {accuracy:.1f}%")
    
    return {
        'weights': weights,
        'bias': bias,
        'epochs': epoch + 1,
        'accuracy': accuracy
    }

def main():
    print("N-INPUT PERCEPTRON FOR LOGIC GATES")
    print("=" * 60)
    
    test_cases = [
        (3, "AND"),
        (3, "OR"),
        (4, "AND"),
        (4, "OR")
    ]
    
    results = {}
    
    for n_inputs, gate_type in test_cases:
        key = f"{n_inputs}_{gate_type}"
        results[key] = train_perceptron(n_inputs, gate_type)
    
    print(f"\n{'='*60}")
    print("FINAL SUMMARY")
    print(f"{'='*60}")
    
    for n in [3, 4]:
        print(f"\n{n}-INPUT GATES:")
        and_key = f"{n}_AND"
        or_key = f"{n}_OR"
        
        print(f"  AND Gate:")
        print(f"    Weights: {results[and_key]['weights']}")
        print(f"    Bias: {results[and_key]['bias']:.3f}")
        print(f"    Epochs: {results[and_key]['epochs']}")
        print(f"    Accuracy: {results[and_key]['accuracy']:.1f}%")
        
        print(f"  OR Gate:")
        print(f"    Weights: {results[or_key]['weights']}")
        print(f"    Bias: {results[or_key]['bias']:.3f}")
        print(f"    Epochs: {results[or_key]['epochs']}")
        print(f"    Accuracy: {results[or_key]['accuracy']:.1f}%")

if __name__ == "__main__":
    main()
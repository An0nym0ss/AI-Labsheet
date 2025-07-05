def heuristic(state, goal):
    return sum(1 for i in range(len(state)) if state[i] != goal[i])

def get_neighbors(state):
    
    neighbors = []
    for i in range(len(state) - 1):
        new_state = state[:]
        new_state[i], new_state[i+1] = new_state[i+1], new_state[i]
        neighbors.append(new_state)
    return neighbors

def hill_climbing(initial_state, goal_state):
    current = initial_state
    path = [current]
    current_h = heuristic(current, goal_state)

    print(f"Initial Stack: {current} | Heuristic: {current_h}")

    while True:
        neighbors = get_neighbors(current)
        scored_neighbors = [(neighbor, heuristic(neighbor, goal_state)) for neighbor in neighbors]

        print("\nGenerated Neighbors:")
        for n, h in scored_neighbors:
            print(f"  {n} | Heuristic: {h}")

        
        best_neighbor, best_h = min(scored_neighbors, key=lambda x: x[1])

        if best_h >= current_h:
            print("\n Hill climbing got stuck! Local optimum reached.")
            return path

        current = best_neighbor
        current_h = best_h
        path.append(current)

        print(f"\nMoved to: {current} | Heuristic: {current_h}")

        if current == goal_state:
            print("\n Goal reached!")
            return path

initial_stack = ['C', 'A', 'D', 'B']
goal_stack = ['A', 'B', 'C', 'D']

solution_path = hill_climbing(initial_stack, goal_stack)

print("\n Solution Path:")
for i, step in enumerate(solution_path):
    print(f"Step {i}: {step}")
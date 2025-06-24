import random

def initialize_environment(rows, cols):
    return [[random.choice([0, 1]) for _ in range(cols)] for _ in range(rows)]

def print_environment(env, agent_pos=None):
    for i, row in enumerate(env):
        line = []
        for j, cell in enumerate(row):
            if (i, j) == agent_pos:
                line.append('A' if cell == 1 else 'a')  # A for agent on dirty, a for agent on clean
            else:
                line.append(str(cell))
        print(' '.join(line))
    print()

def is_clean(env):
    return all(cell == 0 for row in env for cell in row)

def find_nearest_dirty_cell(env, agent_pos):
    rows, cols = len(env), len(env[0])
    i, j = agent_pos
    min_distance = float('inf')
    target = None
    
    for r in range(rows):
        for c in range(cols):
            if env[r][c] == 1:
                distance = abs(r - i) + abs(c - j)  # Manhattan distance
                if distance < min_distance:
                    min_distance = distance
                    target = (r, c)
    return target

def move_towards_target(agent_pos, target):
    i, j = agent_pos
    target_i, target_j = target
    
    if i < target_i:
        return (i + 1, j), 'down'
    if i > target_i:
        return (i - 1, j), 'up'
    if j < target_j:
        return (i, j + 1), 'right'
    if j > target_j:
        return (i, j - 1), 'left'
    return agent_pos, None

def main():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    
    env = initialize_environment(rows, cols)
    print("Initial Environment:")
    agent_pos = (0, 0)
    print_environment(env, agent_pos)
    
    total_cost = 0
    moves = 0
    cleanings = 0
    
    while not is_clean(env):
        i, j = agent_pos
        
        # Clean current cell if dirty
        if env[i][j] == 1:
            env[i][j] = 0
            total_cost += 2
            cleanings += 1
            print(f"Cleaned cell {agent_pos}, cost: 2")
        
        # Find next dirty cell
        target = find_nearest_dirty_cell(env, agent_pos)
        if not target:
            break
            
        # Move towards target
        new_pos, direction = move_towards_target(agent_pos, target)
        if new_pos != agent_pos:
            agent_pos = new_pos
            total_cost += 1
            moves += 1
            print(f"Moved {direction} to {agent_pos}, cost: 1")
        
        print_environment(env, agent_pos)
    
    print("\nFinal Environment:")
    print_environment(env, agent_pos)
    print(f"Total moves: {moves}")
    print(f"Total cleanings: {cleanings}")
    print(f"Total cost: {total_cost}")

if __name__ == "__main__":
    main()
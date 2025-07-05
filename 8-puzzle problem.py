def manhattan(state, goal):
    dist = 0
    for i in range(1, 9):
        x1, y1 = divmod(state.index(i), 3)
        x2, y2 = divmod(goal.index(i), 3)
        dist += abs(x1 - x2) + abs(y1 - y2)
    return dist

def generate_successors(state):
    successors = []
    blank_index = state.index(0)
    row, col = divmod(blank_index, 3)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for i in moves:
        nrow, ncol = row + i[0], col + i[1]
        if 0 <= nrow < 3 and 0 <= ncol < 3:
            new_state = state.copy()
            new_index = nrow * 3 + ncol
            new_state[blank_index], new_state[new_index] = new_state[new_index], new_state[blank_index]
            successors.append(new_state)
    return successors

def main():
    print("Enter the initial state of the puzzle:")
    initialState = list(map(int, input().split()))
    if len(initialState) != 9:
        print("Enter Exactly 9 numbers (0-8) separated by spaces!!!")
        return

    goalstate = [1, 2, 3, 4, 5, 6, 7, 8, 0]

    if initialState == goalstate:
        print("Puzzle Already Solved!!")
        return

    while initialState != goalstate:
        successors = generate_successors(initialState)
        print("Total Successors:", len(successors))
        min_dist = float("inf")
        best_state = None
        for i, succ in enumerate(successors):
            dist = manhattan(succ, goalstate)
            print(f"\nSuccessor {i + 1}:")
            for j in range(0, 9, 3):
                print(succ[j], succ[j + 1], succ[j + 2])
            print(f"Manhattan Distance for successor {i + 1}: {dist}")
            if dist < min_dist:
                min_dist = dist
                best_state = succ
        initialState = best_state
        if best_state != goalstate:
            print("\nBest State:")
            for j in range(0, 9, 3):
                print(best_state[j], best_state[j + 1], best_state[j + 2])
        else:
            print("Puzzle Solved!!")
            for j in range(0, 9, 3):
                print(best_state[j], best_state[j + 1], best_state[j + 2])
            break
if __name__ == "__main__":
    main()
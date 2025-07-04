import random

x, y = map(int, input("Enter the Size of the Grid (x*y): ").split())
grid = [[random.randint(0, 1) for _ in range(y)] for _ in range(x)]

print("Initial grid state:")
for row in grid:
    print(*row)

posX = random.randint(0, x - 1)
posY = random.randint(0, y - 1)
steps = 0

print(f"\nInitial Position: Room[{posX}, {posY}]")

while True:
    # Reflex action: fohor bhaye safaa garne natra randomly move hune
    if grid[posX][posY] == 1:
        grid[posX][posY] = 0
        print(f"Step {steps + 1}: Cleaned Room[{posX}, {posY}].")
    else:
        while True:
            dx = random.randint(-1, 1)
            dy = random.randint(-1, 1)
            newX, newY = posX + dx, posY + dy
            if 0 <= newX < x and 0 <= newY < y:
                posX, posY = newX, newY
                print(f"Step {steps + 1}: Moved to Room[{posX}, {posY}].")
                break
    steps += 1
    # Check sabai safa bhayo ki nai
    if all(cell == 0 for row in grid for cell in row):
        break

print(f"\nAll rooms clean! Total steps = {steps}")
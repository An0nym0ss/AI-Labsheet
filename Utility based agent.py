import random

def abs_val(a):
    return -a if a < 0 else a

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
    if grid[posX][posY] == 1:
        grid[posX][posY] = 0
        print(f"Step {steps + 1}: Cleaned Room[{posX}, {posY}].")
    else:
        # Utility-based: minimal move utilize garne, sabse najeek ko dirty tiles maa jaane
        min_dist = float('inf')
        target = None
        for i in range(x):
            for j in range(y):
                if grid[i][j] == 1:
                    dist = abs_val(i - posX) + abs_val(j - posY)
                    if dist < min_dist:
                        min_dist = dist
                        target = (i, j)
        if not target:
            break
        tx, ty = target
        if tx > posX:
            posX += 1
        elif tx < posX:
            posX -= 1
        elif ty > posY:
            posY += 1
        elif ty < posY:
            posY -= 1
        print(f"Step {steps + 1}: Moved to Room[{posX}, {posY}].")
    steps += 1

print(f"\nAll rooms clean! Total steps = {steps}")
import random
import time


WIDTH = 50
HEIGHT = 20
ALIVE = "█"
DEAD = " "


def make_grid(width, height, chance=0.25):
    return [
        [random.random() < chance for _ in range(width)]
        for _ in range(height)
    ]


def count_neighbors(grid, x, y):
    total = 0

    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            if dx == 0 and dy == 0:
                continue

            nx = (x + dx) % WIDTH
            ny = (y + dy) % HEIGHT

            if grid[ny][nx]:
                total += 1

    return total


def step(grid):
    new_grid = []

    for y in range(HEIGHT):
        row = []

        for x in range(WIDTH):
            alive = grid[y][x]
            neighbors = count_neighbors(grid, x, y)

            if alive and neighbors in (2, 3):
                row.append(True)
            elif not alive and neighbors == 3:
                row.append(True)
            else:
                row.append(False)

        new_grid.append(row)

    return new_grid


def draw(grid, generation):
    print("\033[H\033[J", end="")
    print(f"Conway's Game of Life — Generation {generation}")
    print("+" + "-" * WIDTH + "+")

    for row in grid:
        line = "".join(ALIVE if cell else DEAD for cell in row)
        print("|" + line + "|")

    print("+" + "-" * WIDTH + "+")
    print("Press Ctrl+C to stop.")


def insert_glider(grid, x, y):
    pattern = [
        (1, 0),
        (2, 1),
        (0, 2),
        (1, 2),
        (2, 2),
    ]

    for dx, dy in pattern:
        grid[(y + dy) % HEIGHT][(x + dx) % WIDTH] = True


def insert_blinker(grid, x, y):
    for dx in range(3):
        grid[y % HEIGHT][(x + dx) % WIDTH] = True


def insert_block(grid, x, y):
    for dy in range(2):
        for dx in range(2):
            grid[(y + dy) % HEIGHT][(x + dx) % WIDTH] = True


def clear_grid(width, height):
    return [
        [False for _ in range(width)]
        for _ in range(height)
    ]


def seed_demo_world():
    grid = clear_grid(WIDTH, HEIGHT)

    insert_glider(grid, 2, 2)
    insert_glider(grid, 12, 4)
    insert_blinker(grid, 25, 8)
    insert_blinker(grid, 35, 15)
    insert_block(grid, 42, 3)

    for _ in range(80):
        x = random.randrange(WIDTH)
        y = random.randrange(HEIGHT)
        grid[y][x] = random.choice([True, False, False])

    return grid


def is_empty(grid):
    for row in grid:
        for cell in row:
            if cell:
                return False

    return True


def main():
    grid = seed_demo_world()
    generation = 0

    try:
        while True:
            draw(grid, generation)
            time.sleep(0.12)

            grid = step(grid)
            generation += 1

            if is_empty(grid):
                print("Everything died. Very dramatic.")
                break

    except KeyboardInterrupt:
        print("\nStopped.")


if __name__ == "__main__":
    main()
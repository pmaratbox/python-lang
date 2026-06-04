def step(grid):
    rows, cols = len(grid), len(grid[0])
    new = [[0] * cols for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            live = 0
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if dr == 0 and dc == 0:
                        continue
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        live += grid[nr][nc]
            if grid[r][c] == 1:
                new[r][c] = 1 if live in (2, 3) else 0
            else:
                new[r][c] = 1 if live == 3 else 0
    return new


def main():
    grid = [
        [0, 1, 0],
        [0, 1, 0],
        [0, 1, 0],
    ]
    grid = step(grid)
    for row in grid:
        print("".join("#" if cell else "." for cell in row))


if __name__ == "__main__":
    main()

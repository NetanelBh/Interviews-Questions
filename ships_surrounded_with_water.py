def find_ship(grid, i, j):
    if i == len(grid) or j == len(grid[i]) or grid[i][j] == '.':
        return

    grid[i][j] = '.'
    find_ship(grid, i, j + 1)
    find_ship(grid, i + 1, j)


def num_of_ships(grid):
    count = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'X':
                find_ship(grid, i, j)
                count += 1

    return count


if __name__ == "__main__":
    g = [
        ['X', '.', '.', 'X'],
        ['.', 'X', '.', 'X'],
        ['.', '.', '.', 'X'],
        ['X', '.', 'X', '.'],
    ]

    print(num_of_ships(g))

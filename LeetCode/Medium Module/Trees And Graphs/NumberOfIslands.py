from typing import List


def mark_adjacent_island(grid, i, j, m, n):
    if i != 0 and grid[i-1][j] == "1":
        grid[i-1][j] = "X"
        mark_adjacent_island(grid, i-1, j, m, n)
    if i != m-1 and grid[i+1][j] == "1":
        grid[i+1][j] = "X"
        mark_adjacent_island(grid, i+1, j, m, n)
    if j != 0 and grid[i][j-1] == "1":
        grid[i][j-1] = "X"
        mark_adjacent_island(grid, i, j-1, m, n)
    if j != n-1 and grid[i][j+1] == "1":
        grid[i][j+1] = "X"
        mark_adjacent_island(grid, i, j+1, m, n)

    return grid


def numIslands(grid: List[List[str]]) -> int:
    m = len(grid)
    n = len(grid[0])
    count = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1":
                grid = mark_adjacent_island(grid, i, j, m, n)
                count += 1

    return count


print(numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))

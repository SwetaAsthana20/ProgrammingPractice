def get_min_distance(grid, i, j, m, n, result):
    if grid[i][j] == 9:
        return result

    if i != 0 and grid[i - 1][j] in [1,9]:
        if grid[i - 1][j] != 9:  grid[i - 1][j] = "X"
        temp = get_min_distance(grid, i - 1, j, m, n, result + 1)
        if temp:
            return temp
    if i != m - 1 and grid[i + 1][j] in [1,9]:
        if grid[i + 1][j] != 9:  grid[i + 1][j] = "X"
        temp = get_min_distance(grid, i + 1, j, m, n, result + 1)
        if temp:
            return temp
    if j != 0 and grid[i][j - 1] in [1,9]:
        if grid[i][j-1] != 9:  grid[i][j-1] = "X"
        temp = get_min_distance(grid, i, j - 1, m, n, result + 1)
        if temp:
            return temp
    if j != n - 1 and grid[i][j + 1] in [1,9]:
        if grid[i][j+1] != 9:  grid[i][j+1] = "X"
        temp = get_min_distance(grid, i, j + 1, m, n, result + 1)
        if temp:
            return temp


def minimumDistance(area):
    # Write your code here
    if area and area[0][0] == 1:
        m = len(area)
        n = len(area[0])
        area[0][0] = "X"
        print(get_min_distance(area, 0, 0, m, n, 0))
    else:
        return -1

minimumDistance([[1,0,0],
[1,0,0],
[1,9,1]]
)
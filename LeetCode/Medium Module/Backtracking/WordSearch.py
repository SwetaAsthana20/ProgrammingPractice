def check_next(board, row, col, letter):
    if not letter:
        return True
    if row > len(board) - 1 or row < 0 or col > len(board[0]) - 1 or col < 0 or letter[0] != board[row][col]:
        return False
    board[row][col] = "#"
    res = check_next(board, row + 1, col, letter[1:]) or check_next(board, row - 1, col, letter[1:]) or check_next(
        board, row, col + 1, letter[1:]) or check_next(board, row, col - 1, letter[1:])
    board[row][col] = letter[0]
    return res


def exist(board, word):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if check_next(board, i, j, word):
                return True

    return False


print(exist([["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]], "AAB"))

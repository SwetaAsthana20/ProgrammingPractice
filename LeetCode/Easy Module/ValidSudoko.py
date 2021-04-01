from typing import List


def isValidSudoku(board: List[List[str]]) -> bool:
    for i in board:
        temp_set = []
        for j in range(0, 9):
            if i[j].isdigit() and i[j] in temp_set:
                return False
            elif i[j].isdigit():
                temp_set.append(i[j])

    for i in range(0, 9):
        temp_set = []
        for j in range(0, 9):
            if board[j][i].isdigit() and board[j][i] in temp_set:
                return False
            elif board[j][i].isdigit():
                temp_set.append(board[j][i])

    x = 0
    y = 0
    counter = 0
    while counter < 9:
        temp_set = []
        for i in range(x, x + 3):
            for j in range(y, y + 3):
                if board[i][j].isdigit() and board[i][j] in temp_set:
                    return False
                elif board[i][j].isdigit():
                    temp_set.append(board[i][j])
        y += 3
        if counter in [2, 5]:
            x = x + 3
            y = 0
        counter += 1

    return True


print(isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))


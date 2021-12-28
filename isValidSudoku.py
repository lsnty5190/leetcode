board = [
    ["9",".",".","6",".",".",".",".","."],
    [".",".",".",".","6",".",".",".","."],
    [".",".",".",".",".","1",".","3","."],
    [".",".",".",".",".",".",".",".","8"],
    [".",".",".",".",".","8",".",".","."],
    [".",".",".","4",".",".","2",".","."],
    [".",".",".",".",".",".",".",".","1"],
    ["6",".",".",".","1",".",".",".","."],
    [".",".",".",".",".",".",".",".","."]
]


def check_unit(unit):

    unit = [i for i in unit if i != '.']

    return len(set(unit)) == len(unit)

def check_row():

    for row in board:
        if not check_unit(row):
            return False
    return True

def check_col():

    for col in zip(*board):
        if not check_unit(col):
            return False
    return True

def check_round(cord):

    unit = []
    for pos in [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1), (0, 0)]:
        x, y = pos
        if board[cord[0]+x][cord[1]+y] != '.': unit.append(board[cord[0]+x][cord[1]+y])
    return len(set(unit)) == len(unit)

def check_square():

    cent = [(1, 1), (1, 4), (1, 7), (4, 1), (4, 4), (4, 7), (7, 1), (7, 4), (7, 7)]

    for pos in cent:
        if not check_round(pos):
            return False
    return True

def check_board():

    return check_row() and check_col() and check_square()

res = check_board()
print(res)


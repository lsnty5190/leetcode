board = [["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","B"],["A","A","A","A","B","A"]]

word = "AAAAAAAAAAAAABB"
length = len(board)
width = len(board[0])

# print(length, width)

def dfs(pos, path, step, visited: set, res):

    if word == ''.join(path):
        res.append(path)
        return

    x, y = pos

    if x < 0 or x >= length or y < 0 or y >= width or word[step] != board[x][y] or pos in visited:
        return

    # print(pos)
    visited.add(pos)

    for cord in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        cur_pos = (x+cord[0], y+cord[1])
        dfs(cur_pos, path+[board[x][y]], step+1, visited, res)
    
    visited.remove(pos)

def exist():


    for i in range(length):
        for j in range(width):
            res = []
            visited = set()
            dfs((i, j), [], 0, visited, res)
            if bool(res) is True:
                return True

    return False

res = exist()
print(res)

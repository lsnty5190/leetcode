# https://leetcode.com/problems/01-matrix/

from collections import deque

queue = deque()

mat = [[0,0,0],[0,1,0],[1,1,1]]

visited = set()

for i in range(len(mat)):
    for j in range(len(mat[0])):
        if mat[i][j] == 0:
            queue.append((i,j))
            visited.add((i,j))

# BFS with queue
while queue:
    x, y = queue.popleft()
    for ord in [(1,0), (-1,0), (0,1), (0,-1)]:
        newx, newy = x+ord[0], y+ord[1]
        # bound
        if newx >=0 and newx <= len(mat)-1 and newy >=0 and newy <= len(mat[0])-1 and (newx,newy) not in visited:
            # add a step
            mat[newx][newy] = mat[x][y] + 1
            queue.append((newx,newy))
            visited.add((newx,newy))

print(mat)
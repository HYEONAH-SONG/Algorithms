from collections import deque
import sys

dx = [1,-1,0,0]
dy = [0,0,-1,1]


# matrix = [list(map(int,input().split())) for _ in range(n)]
# print(matrix)

def iswall(x,y):
    if x<0 or y<0 :
        return False
    if x >= n or y >= m :
        return False
    if matrix[x][y] == 0 : # 방문한 경우
        return False
    return True # 그 외의 경우

def bfs(x,y):
    queue = deque()
    print(queue)
    queue.append((x, y))
    print(queue)
# queue = deque((x,y)) # 시작 지점을 넣는다.
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if iswall(nx,ny) and matrix[nx][ny]==1:
                matrix[nx][ny] = matrix[x][y]+1
                queue.append((nx,ny))
    return matrix[n-1][m-1]

n,m = map(int,input().split())
matrix = [[1, 1, 0], [0, 1, 0], [0, 1, 1]]
print(bfs(0,0))

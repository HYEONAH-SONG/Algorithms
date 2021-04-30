from collections import deque
import sys
sys.stdin = open("input.txt")

line, chick = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(line)]
print(matrix)

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def iswall(x,y):
    if matrix[x][y] ==0:
        return False
    if matrix[x][y] ==1:
        return False
    if x<0 or y<0:
        return False
    if x>=line or y>=line :
        return False
    return True

def bfs(x,y):
    queue = deque((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if iswall(nx,ny): # 2인 경우 (치킨집)
                if matrix[x][y]==1:


min_num = 0
for i in range(line):
    for j in range(line):
        if matrix[i][j]==1:
            min_num+= bfs(i,j)
print(min_num)
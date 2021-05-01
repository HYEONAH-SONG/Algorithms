# 적록색약은 빨간색과 초록색의 차이를 느끼지 못함
# 같은 색으로 이루어진 구역의 갯수를 구하기
# 적록색약인 사람과 아닌 사람이 봤을 때 구역의 갯수 구하기

import sys
from collections import deque

sys.stdin = open("input.txt")
line = int(input())
matrix = [list(input()) for _ in range(line)]
visited = [[0 for _ in range(line)] for _ in range(line)]

# 상 하 우 좌
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def iswall(nx,ny): # 벽이 되는 조건
    if nx < 0 or ny < 0: # 좌표가 0 미만이 되는 경우
        return False
    if nx >= line or ny >= line: # 좌표가 16을 넘는 경우
        return False
    if visited[nx][ny] == 1: # 좌표값이 1인 경우 --> 방문했던 곳은 재방문 x
        return False
    return True


def bfs(x,y):
    queue = deque()
    queue.append((x, y)) # 출발 지점
    visited[x][y] = 1 # 출발 지점을  1 (방문 표시)
    while queue:
        x,y = queue.popleft() # 좌표
        visited[x][y]=1 # 도착 지점에 도착하지 않은 경우 방문 표시
        for i in range(4): # 상 하 좌 우 좌표 살피기
            nx,ny=x+dx[i],y+dy[i]
            if iswall(nx,ny) : # 막혀있지 않은 경우
                if matrix[nx][ny] == matrix[x][y]: # 벽이 없는 경우 &  색이 같은 경우
                    queue.append((nx, ny))
                    visited[nx][ny] = 1

cnt = 0
# 0 ~ line -1
for i in range(line):
    for j in range(line):
        if visited[i][j]==0: # 방문 안한 경우
            bfs(i,j)
            cnt+=1
print(cnt, end=" ")
#-------------------- 적록 색약 -------------------#
# 0 ~ line -1
for i in range(line):
    for j in range(line):
        if matrix[i][j] =='R': # 방문 안한 경우
            matrix[i][j] ='G'
visited = [[0 for _ in range(line)] for _ in range(line)]

cnt = 0
# 0 ~ line -1
for i in range(line):
    for j in range(line):
        if visited[i][j] == 0: # 방문 안한 경우
            bfs(i,j)
            cnt+=1
print(cnt)
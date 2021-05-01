import sys
from collections import deque

sys.stdin = open("input.txt")

N,L,R = map(int,input().split())

matrix = [list(map(int,input().split())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]

# 상 하 우 좌
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def iswall(nx,ny): # 벽이 되는 조건
    if nx < 0 or ny < 0: # 좌표가 0 미만이 되는 경우
        return False
    if nx >= N or ny >= N: # 좌표가 16을 넘는 경우
        return False
    if visited[nx][ny] == 1: # 좌표값이 1인 경우 --> 방문했던 곳은 재방문 x
        return False
    return True

def bfs(x,y):
    queue = deque()
    queue.append((x, y)) # 출발 지점
    visited[x][y] = 1 # 출발 지점을  1 (방문 표시)
    avilable = []
    avilable.append((x,y))
    while queue:
        x,y = queue.popleft() # 좌표
        visited[x][y]=1 # 도착 지점에 도착하지 않은 경우 방문 표시
        for i in range(4): # 상 하 좌 우 좌표 살피기
            nx,ny=x+dx[i],y+dy[i]
            if iswall(nx,ny) : # 막혀있지 않은 경우
                if L<= abs(matrix[nx][ny] - matrix[x][y])<=R:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
                    avilable.append([nx,ny]) # 가능한 국경 좌표 리스트
    return avilable

count = 0
# 0 ~ line -1

for i in range(N):
    for j in range(N):
        if visited[i][j] == 0 :
            temp = bfs(i,j)

print(temp)
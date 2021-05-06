from collections import deque
N,M = 5,6
matrix = [[0,0,1,1,0],[0,0,0,1,1],[1,1,1,1,1],[0,0,0,0,0]]

# 상 하 우 좌
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
count = 0
def iswall(nx,ny): # 벽이 되는 조건
    if nx < 0 or ny < 0: # 좌표가 0 미만이 되는 경우
        return False
    if nx >= 4 or ny >= 5: # 좌표가 16을 넘는 경우
        return False
    if matrix[nx][ny] == 1: # 좌표값이 1인 경우 --> 방문했던 곳은 재방문 x
        return False
    return True

def bfs(x,y):
    queue = deque()
    queue.append((x, y)) # 출발 지점
    matrix[x][y] = 1 # 출발 지점을  1 (방문 표시)
    while queue:
        x,y = queue.popleft() # 좌표
        matrix[x][y]=1 # 도착 지점에 도착하지 않은 경우 방문 표시
        for i in range(4): # 상 하 좌 우 좌표 살피기
            nx,ny=x+dx[i],y+dy[i]
            if iswall(nx,ny) : # 막혀있지 않은 경우
                queue.append((nx, ny))

for i in range(4):
    for j in range(5):
        if matrix[i][j] ==0:
            bfs(i,j)
            count +=1
print(count)
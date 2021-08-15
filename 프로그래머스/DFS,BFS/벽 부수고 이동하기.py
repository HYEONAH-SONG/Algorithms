import sys
sys.stdin = open("input.txt")

from collections import deque

# 벽인 경우, 인덱스 초과한 경우 --> 지나갈 수 없음
def iswall(nx,ny):
    if nx < 0 or ny < 0:
        return False
    if nx >= N or ny >= M:
        return False
    if matrix[nx][ny] == 1:
        return False
    return True

def bfs(end_x,end_y):
    queue = deque()
    queue.append((0,0,1))
    visited = [[0 for _ in range(M)] for _ in range(N)]
    visited[0][0] = 1
    while queue:
        x,y,cnt = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if iswall(nx,ny) and visited[nx][ny] == 0: # 미로를 계속 진행할 수 있는 경우
                if nx == end_x and ny == end_y:
                    return cnt + 1
                queue.append((nx,ny,cnt+1))
                visited[nx][ny] = 1
        return -1

global N, M
N, M = map(int,input().split())
matrix = [list(map(int,input())) for _ in range(N)]
# 상 하 좌 우
dx = [0,0,1,-1]
dy = [1,-1,0,0]

print(bfs(N-1,M-1))


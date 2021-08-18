import sys
sys.stdin = open("input.txt")

from collections import deque

# 지나갈 수 있는지 여부 판단 함수
def iswall(nx,ny):
    # 맵의 경계 내부에 존재하지 않는 경우
    if nx < 0 or ny < 0:
        return False
    if nx >= N or ny >= M:
        return False
    return True

def bfs(end_x,end_y):
    queue = deque()
    queue.append((0,0,K))
    visited = [[[0]*(K+1) for _ in range(M)] for _ in range(N)]
    visited[0][0][K] = 1 # 출발지점(좌표 + 횟수(벽을 한번도 부수지 않음)
    while queue:
        x,y,check = queue.popleft() # check = 벽을 부술 수 있는 횟수

        # 도착 지점에 도착한 경우
        if x == end_x and y == end_y:
            return visited[x][y][check]
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            # 지나갈 수 있는 경로인 경우
            if iswall(nx,ny) and not visited[nx][ny][check]: # 이 부분이 핵심 포인트 !!!!
                # 도착하지 않은 경우
                # 1. 벽이 아니고 방문한 적이 없는 경우
                if not matrix[nx][ny] :
                    queue.append((nx,ny,check))
                    visited[nx][ny][check] = visited[x][y][check]+1

                # 2. 벽이고 벽이 부술 수 있는 경우(check >= 1)
                elif matrix[nx][ny] and check:
                    visited[nx][ny][check-1] = visited[x][y][check] + 1
                    queue.append((nx,ny,check-1)) # 벽이 부숴졌기 때문에
    return -1

# -----------------Initialized Part --------------------
global N, M, K
N, M, K  = map(int,input().split())
matrix = [list(map(int,input())) for _ in range(N)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]
print(bfs(N-1,M-1))

import sys
sys.stdin = open("input.txt")

from collections import deque

def iswall(nx,ny):
    if nx < 0 or ny < 0:
        return False
    if nx >= N or ny >= M:
        return False
    if matrix[nx][ny] == 0:
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
            if iswall(nx,ny) and visited[nx][ny] == 0:
                if nx == end_x and ny == end_y:
                    return cnt + 1
                queue.append((nx,ny,cnt+1))
                visited[nx][ny] = 1
global N, M
N, M = map(int,input().split())
matrix = [list(map(int,input())) for _ in range(N)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]

print(bfs(N-1,M-1))

# (0,0) -> queue에 출발점 넣음
# queue 에 하나씩 꺼내서 4방향 보고
# 하나씩 본것을 갈 수 있는지 없는지 판별
# Basic template
# sorting system
# inswall --> 벽인지 판단하는 함수
# python algorithm
# python algorithms
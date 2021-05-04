from collections import deque

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
            if iswall(nx,ny) and visited[nx][ny] == 0:
                if nx == end_x and ny == end_y:
                    return cnt + 1
                queue.append((nx,ny,cnt+1))
                visited[nx][ny] = 1


N,M = 3,3
dx = [0,0,1,-1] # 하 상 우 좌
dy = [1,-1,0,0]
cost = 0


matrix = [[0,0,0],[0,0,0],[0,0,0]]
print(bfs(N-1,M-1))
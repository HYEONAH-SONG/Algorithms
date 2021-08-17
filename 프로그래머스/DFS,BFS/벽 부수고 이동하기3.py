# 정답!
# 벽 부수고 이동하기 1과의 차이점 ==> 벽을 부술 수 있는 기회가 있다고 방문 안한다는 보장이 없다.
# 벽을 부술 수 있는 횟수 / 벽을 부순 횟수 --> 다른 시간이 나옴
# check 변수의 증가 타이밍
import sys
sys.stdin = open("input.txt")

from collections import deque

# 지나갈 수 있는지 여부 판단 함수
def iswall(nx,ny,check):
    # 맵의 경계 내부에 존재하지 않는 경우
    if nx < 0 or ny < 0:
        return False
    if nx >= N or ny >= M:
        return False
    if visited[nx][ny][check]:
        return False
    return True

def bfs(end_x,end_y):
    queue = deque()
    queue.append((0,0,0))
    visited[0][0][0] = 1 # 출발지점(좌표 + 횟수(벽을 한번도 부수지 않음)
    while queue:
        x,y,check = queue.popleft() # check = 벽을 부순 횟수

        # 도착 지점에 도착한 경우
        if x == end_x and y == end_y:
            return visited[x][y][check]

        for i in range(4):
            nx, ny, update = x+dx[i], y+dy[i],check+1

            # 지나갈 수 있는 경로인 경우
            if iswall(nx,ny,check):
                # 1. 벽이 아니고 방문한 적이 없는 경우
                if not matrix[nx][ny] :
                    queue.append((nx,ny,check))
                    visited[nx][ny][check] = visited[x][y][check]+1

                # 2. 벽이고 벽이 부술 수 있는 경우(check <= K)
                elif matrix[nx][ny] and update <= K:
                    visited[nx][ny][update] = visited[x][y][check] + 1
                    queue.append((nx,ny,update)) # 벽이 부숴졌기 때문에
    return -1


# -----------------Initialized Part --------------------
global N, M, K
N, M, K  = map(int,input().split())
matrix = [list(map(int,input())) for _ in range(N)]
visited = [[[0]*(K+1) for _ in range(M)] for _ in range(N)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
print(bfs(N-1,M-1))

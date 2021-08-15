from collections import deque

# BFS 메서드 정의
def bfs(x,y):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([x,y])
    queue.append((x,y))
    # 큐가 빌 때(다 돌때까지) 까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력하기
        v = queue.popleft()
        print(v,end=" ")
        # 아직 방문하지 ㅇ낳은 인접한 원소들을 큐에 삽입
        # 현재 위치에서 4가지 방향으로의 위치를 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우는 무시
            if nx < 0 or nx >= n or ny<0 or ny>= m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n-1][m-1]

# N, M을 공백을 기준으로 구분하여 입력 받기
n,m = map(int,input().split())
# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

# 이동할 네 가지 방향 정의(싱, 하, 좌, 우)
dx = [-1,1,0,0]
dy = [0,0,-1,1]
print(bfs(0,0))
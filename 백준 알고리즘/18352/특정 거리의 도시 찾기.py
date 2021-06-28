import sys
from collections import deque

sys.stdin = open("input.txt")

N, M, K, X = map(int, input().split()) # 도시의 개수, 도로의 개수, 최단거리 , 출발 도시의 번호
visited = [0] * (N + 1)
answer = []
path = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split()) # A -> B 로 이동하는 단방향
    path[A].append(B)
# ----------------------------------------initialized------------------------------------------#

q = deque()
q.append((X, 0))
visited[X]=1
while q:
    start, short = q.popleft() # 출발 도시, 최단 거리
    if short == K:
        answer.append(start)
    elif short < K:
        for i in path[start]:
            if not visited[i]: # 아직 방문을 안한 경우
                visited[i] = 1
                q.append((i, short + 1))
# -----------------------------------BFS---------------------------------------------------------#

# 최단 거리가 k인 도시가 존재하지 않는 경우
if len(answer) == 0:
    print(-1)
else: # 존재하는 경우 --> 오름차순으로 출력
    answer.sort()
    for i in answer:
        print(i)
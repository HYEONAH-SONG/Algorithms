# input
# 5 6 --> 정점의 갯수, 간선의 갯수
# 1 --> 시작 정점의 번호
# 5 1 1 --> 각 간선(u -> v, w)
# 1 2 2
# 1 3 3
# 2 3 4
# 2 4 5
# 3 4 6


# output
# 0
# 2
# 3
# 7
# INF

# 방향 그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램을 작성하시오.

import heapq
import sys
sys.stdin = open("input.txt")
V,E = map(int,input().split()) # 정점의 갯수/간선의 갯수
start_point = int(input()) # 시작 정점의 번호

data =[[] for _ in range(V+1)]
for _ in range(E):
    start, end, cost = map(int, input().split())
    data[start].append((end,cost))

# ---------------------------------------------------------------
distance = [float('INF') for _ in range(V+1)]
visited = [0 for _ in range(V+1)]

distance[start_point] = 0

heap = []
heapq.heappush(heap,(0,start_point))

while heap:
    dis,location = heapq.heappop(heap)
    for arrive, cost in data[location]:
        candidate = dis + cost
        if candidate<distance[arrive]: # 더 작은 경우 갱신
            distance[arrive]=candidate
            heapq.heappush(heap,(distance[arrive],arrive))

for i in range(1,V+1):
    if distance[i] == float('INF'):
        print("INF")
    else :
        print(distance[i])
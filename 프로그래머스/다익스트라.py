import sys
import heapq
sys.stdin = open("input.txt")
# 선언
V,E = map(int,input().split())


matrix = [[] for _ in range(V+1)]
for _ in range(E):
    start,end, cost = map(int,input().split())
    matrix[start].append([end,cost])
print(matrix)

start_node = int(input())
distance = [float('INF') for _ in range(V+1)]
distance[start_node] = 0

heap = []
heapq.heappush(heap,(0,start_node))

while heap:
    weight,location = heapq.heappop(heap)
    for near, cost in matrix[location]:
        # 갱신
        if weight + cost < distance[near]:
            distance[near] = weight + cost
            heapq.heappush(heap,(distance[near],near))
print(distance)


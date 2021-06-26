import heapq
V,E = map(int,input().split())
data =[[] for _ in range(V+1)]
for _ in range(E):
    start, end, cost = map(int, input().split())
    data[start].append((end,cost))

start_point = int(input())

distance = [float('INF') for _ in range(V+1)]
visited = [0 for _ in range(V+1)]

distance[start_point] = 0

heap = []
heapq.heappush(heap,(0,start_point))

while heap:
    dis,location = heapq.heappop(heap)
    if location == end:
        break
    for arrive, cost in data[location]:
        candidate = dis + cost
        if candidate<distance[arrive]:
            distance[arrive]=candidate
            heapq.heappush(heap,(distance[arrive],arrive))
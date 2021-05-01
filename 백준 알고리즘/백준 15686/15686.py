from collections import deque
from itertools import combinations

import sys
sys.stdin = open("input.txt")

line, M = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(line)]
print(matrix)

# dx = [0,0,1,-1]
# dy = [1,-1,0,0]
#
# def iswall(x,y):
#     if matrix[x][y] ==0:
#         return False
#     if x<0 or y<0:
#         return False
#     if x>=line or y>=line :
#         return False
#     return True

# def bfs(x,y):
#     queue = deque((x,y))
#     while queue:
#         x,y = queue.popleft()
#         for i in range(4):
#             nx, ny = x + dx[i], y + dy[i]
#             if iswall(nx,ny): # 2인 경우 (치킨집)
#                 if matrix[nx][ny]==1:
#                     house.append((nx,ny))
#                 elif matrix[nx][ny]==2:
#                     chick.append((nx,ny))
#                 queue.append((nx,ny))


chick = []
house = []
minv = float('inf')
for i in range(line):
    for j in range(line):
        if matrix[i][j]==1:
            house.append((i,j))
        elif matrix[i][j]==2:
            chick.append((i, j))
for ch in combinations(chick,M):
    sum = 0
    for h in house:
        sum +=min([abs(h[0]-i[0])+abs(h[1]-i[1]) for i in chick])
        if minv <=sum :break
    if sum < minv : minv =sum
print(minv)

# sum =0
# for ch in combinations(chick,M):
#     for h in house:
#         sum +=min([abs(h[0]-i[0])+abs(h[1]-i[1]) for i in chick])
# print(sum)
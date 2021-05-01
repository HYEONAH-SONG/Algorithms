from collections import deque
from itertools import combinations

# import sys
# sys.stdin = open("input.txt")

line, M = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(line)]

chick = []
house = []

for i in range(line):
    for j in range(line):
        if matrix[i][j]==1:
            house.append((i,j))
        elif matrix[i][j]==2:
            chick.append((i, j))
m_list =[]
for ch in combinations(chick, M):
    sum = 0
    for h in house:
        sum += min([abs(h[0] - i[0]) + abs(h[1] - i[1]) for i in ch])
    m_list.append(sum)
print(min(m_list))



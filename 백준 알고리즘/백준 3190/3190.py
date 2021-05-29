# matrix  최대 사이즈 : 100 x 100 => 10000
# 최악의 경우 : 뱀이 끝까지 돌고 난 후에 자신의 몸과 부딪히는 경우
# 시간 복잡도
# y는 위 아래 --> Row / x는 왼, 오른쪽 --> col
from collections import deque
import sys
sys.stdin = open("input.txt")

# 상 우 하 좌
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def iswall(x, y):
    if x < 0 or y < 0 :
        return False
    if x >= N or y >= N :
        return False
    if matrix[y][x] ==2 :
        return False
    return True

def bfs():
    direction = 1  # 초기 방향
    time = 1  # 시간
    x, y = 0, 0  # 초기 뱀 위치
    visited = deque([[y, x]])  # 방문 위치
    matrix[y][x] = 2
    while True:
        y, x = y + dy[direction], x + dx[direction]
        if 0 <= y < N and 0 <= x < N and matrix[y][x] != 2:
            if not matrix[y][x] == 1:  # 사과가 없는 경우
                temp_y, temp_x = visited.popleft()
                matrix[temp_y][temp_x] = 0  # 꼬리 제거
            matrix[y][x] = 2
            visited.append([y, x])
            if time in times.keys():
                direction = change(direction, times[time])
            time += 1
        else:  # 본인 몸에 부딪히거나, 벽에 부딪힌 경우
            return time

# -----------------------------------------initialize -----------------------------------------
# matrix size
N = int(input())
matrix = [[0] * N for _ in range(N)]

# number of apple
K = int(input())
for _ in range(K):
    a, b = map(int, input().split())
    matrix[a - 1][b - 1] = 1  # 사과 좌표
# 뱀의 방향 변환 정보
L = int(input())
times = {}
for i in range(L): # X : 시간, C : 방향
    X, C = input().split()
    times[int(X)] = C
print(bfs())
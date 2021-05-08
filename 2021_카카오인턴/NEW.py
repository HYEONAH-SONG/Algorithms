from collections import deque

# places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
visited = [[0 for _ in range(5)] for _ in range(5)]

# 상 하 우 좌
dx = [0, 0, 1, -1, 1,1,-1,-1,0, 0, 2, -2]
dy = [1, -1, 0, 0,1,-1,1,-1,2, -2, 0, 0]

def iswall(x, y):
    if x < 0 or y < 0 :
        return False
    if x >= 5 or y >= 5 :
        return False

    return True

def bfs(x,y,matrix):
    queue = deque()
    queue.append((x, y))
    # visited[x][y] = 1 # 방문 표시
    while queue:
        x, y= queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if iswall(nx, ny) :
                if matrix[nx][ny]=="P": # 착석
                    return 0
                continue
        for i in range(4,8):
            nx, ny = x + dx[i], y + dy[i]
            if iswall(nx, ny) :
                if matrix[nx][ny] == "P":
                    if matrix[x][ny]=="X" and  matrix[nx][y]=="X":  # 착석
                        continue
                    else:
                        # print(nx,ny)
                        return 0

        for i in range(8, 12):
            nx, ny = x + dx[i], y + dy[i]
            nnx,nny = x+ dx[i-8],y + dy[i-8]
            if iswall(nx, ny) :
                if matrix[nx][ny] == "P" and matrix[nnx][nny]!="X":  # 착석
                    # print(nx, ny)
                    return 0


def check(matrix): # 각 대기실에서 거리두기가 지켜지는 지를 확인
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == "P": # 착석한 좌표
                # print(bfs(i, j,matrix))
                if bfs(i, j,matrix) ==False:
                    return False
                else:
                    continue # 안전한지 판단
    return True

def solution(places):
    answer = []
    for i in places:
        print(i)
        if check(i) == True:
            answer.append(1)
        else:
            answer.append(0)
    return answer
#
# print(solution(places))


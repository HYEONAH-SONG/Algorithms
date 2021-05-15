from collections import deque

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

# 거리가 2 이하인 방향
dx = [0, 0, 1, -1, 1, 1, 1, -1, 0, 0, 2, -2]
dy = [1, -1, 0, 0, 1, -1, 1,-1, 2, -2, 0, 0]

def iswall(x, y):
    if x < 0 or y < 0 :
        return False
    if x >= 5 or y >= 5 :
        return False
    return True
# 방문 표시가 필요 없음 --> 방문 표시 해서 시간이 오래 걸림

def bfs(x,y,matrix):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y= queue.popleft()
        for i in range(4): # 한칸 상하좌우
            nx, ny = x + dx[i], y + dy[i]
            if iswall(nx, ny) :
                if matrix[nx][ny]=="P": # 안되는 경우 : 자신의 상하좌우에 사람이 존재하는 경우
                    return 0
                continue
        for i in range(4,8): # 대각선
            nx, ny = x + dx[i], y + dy[i]
            if iswall(nx, ny) :
                if matrix[nx][ny] == "P":
                    if matrix[x][ny]=="X" and  matrix[nx][y]=="X":  # 되는 경우는 대각선 사람과 자신 사이에 칸막이가 존재하는 경우
                        continue
                    else:
                        # print(nx,ny)
                        return 0

        for i in range(8, 12): # 두칸 상하좌우
            nx, ny = x + dx[i], y + dy[i]
            nnx,nny = x+ dx[i-8],y + dy[i-8]
            if iswall(nx, ny) :
                if matrix[nx][ny] == "P" and matrix[nnx][nny]!="X":  # 안되는 경우 : 옆에 칸막이가 없는데 그 다음에 사람이 앉은 경우
                    # print(nx, ny)
                    return 0

def check(matrix): # 각 대기실에서 거리두기가 지켜지는 지를 확인
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == "P": # 착석한 좌표 --> P를 기준으로 거리 2 이내만 판단한다
                # print(bfs(i, j,matrix))
                if bfs(i, j,matrix) ==False: # 하나라도 False 가 나오면 바로 return False
                    return False
                else:
                    continue #끝까지 진행
    return True

def solution(places):
    answer = []
    for i in places: # 5개의 대기실을 순차적으로 판단
        if check(i) == True: # 거리 두기를 한 경우
            answer.append(1)
        else: # 거리 두기를 지키지 못한 경우
            answer.append(0)
    return answer

print(solution(places))
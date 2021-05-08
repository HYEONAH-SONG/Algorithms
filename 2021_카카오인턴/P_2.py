from collections import deque
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def iswall(nx,ny):
    if nx < 0 or ny < 0:
        return False
    if nx >= 5 or ny >= 5:
        return False
    if visited[nx][ny] == 1:
        return False
    return True

def check(matrix): # 각 대기실에서 거리두기가 지켜지는 지를 확인
    location=[]
    location_X = []
    for i in range(5):
        for j in range(5):
            if matrix[i][j]=="P": # 착석
                location.append([i,j])
            if matrix[i][j]=="X": # 칸막이
                location_X.append([i,j])
    if not location: # P가 없는 경우
        return 1

def bfs(board):
    p_lo = []
    x_lo=[]
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = 1 # 방문 표시
    while queue:
        x, y= queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if iswall(nx, ny) and visited[nx][ny] == 0:
                if board[nx][ny]=="P": # 착석
                    if p_lo:
                        px,py=p_lo.pop()
                        dista
                    p_lo.append((nx,ny))
                if board[nx][ny]=="X": # 착석
                    x_lo.append((nx,ny))
                if nx == 5 and ny == 5:
                    return 1
                queue.append((nx, ny))
                visited[nx][ny] = 1

    # print("location")
    # print(location)
    # print("location_X")
    # print(location_X)
    # 맨핸튼 거리가 2 이하이면서 파티션이 없는 경우 제외 다 허용


def solution(places):
    answer = []
    for i in places:
        print(i)
        if check(i) == True:
            answer.append(check(i))
    return answer
visited = [[0 for _ in range(5)] for _ in range(5)]
places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(places))
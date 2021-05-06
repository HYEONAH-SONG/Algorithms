from collections import deque


def solution(matrix):
    N, M = len(matrix), len(matrix)
    dx = [0, -1, 0, 1]  # 하 상 우 좌
    dy = [-1, 0, 1, 0]

    def iswall(nx, ny):
        if nx < 0 or ny < 0:
            return False
        if nx >= N or ny >= M:
            return False
        if matrix[nx][ny] == 1:
            return False
        return True

    def bfs(start):
        queue = deque([start])
        # queue.append([start]) # 출발 지점
        matrix[0][start[0]]= 1 # 출발 지점을  1 (방문 표시)
        stack = []
        visited = [[10000000000] * N for _ in range(M)]
        visited[0][0] = 0
        while queue:
            # print(queue)
            x,y,cost,head = queue.popleft() # 좌표
            # matrix[x][y]=0 # 도착 지점에 도착하지 않은 경우 방문 표시
            for i in range(4): # 상 하 좌 우 좌표 살피기
                nx,ny=x+dx[i],y+dy[i]
                if iswall(nx,ny) : # 막혀있지 않은 경우
                    if head != i:
                        n_cost =cost+ 600
                    else :
                        n_cost = cost + 100
                    if n_cost < visited[nx][ny]:
                        visited[nx][ny] = n_cost
                        queue.append([nx, ny, n_cost, i])
                    # if nx == N - 1 and ny == M - 1:  # 도착한 경우
                    #     cost_list.append(n_cost)
                    #     # print(cost_list)
                    #     # return cost
                    # queue.append((nx, ny,n_cost,i))
                    # print(stack)
        return visited[-1][-1]
    return min(bfs((0,0,0,2)),bfs((0,0,0,3)))
#----------------------------initialized ---------------------#
matrix =[[0,0,0],[0,0,0],[0,0,0]]
print(solution(matrix))
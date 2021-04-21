# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성
# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
# 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.
from collections import deque
import sys
#sys.stdin = open("input.txt")

N,M,V=map(int,input().split()) # node, edge, node number
matrix=[[0]*(N+1) for i in range(N+1)]

for i in range(M):
    a,b = map(int,input().split())
    matrix[a][b]=matrix[b][a]=1
visit=[0]*(N+1)

def dfs(V):
    visit[V]=1 #방문한 점 1로 표시
    print(V, end=' ')
    for i in range(1,N+1):
        if(visit[i]==0 and matrix[V][i]==1):
            dfs(i)

def bfs(V):

    queue=deque([V]) #들려야 할 정점 저장
    visit[V]=0 #방문한 점 0으로 표시
    while queue:
        V=queue.popleft()
        print(V, end=' ')
        for i in range(1, N+1):
            if(visit[i]==1 and matrix[V][i]==1): #방문 안한 경우
                queue.append(i)
                visit[i]=0

dfs(V)
print()
bfs(V)
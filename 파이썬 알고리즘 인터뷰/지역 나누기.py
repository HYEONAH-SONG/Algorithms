# 상하좌우를 살펴본 뒤에 주변 지점 중에서 값이 '0'이면서 아직 방문하지 않은 지점이 있다면 해당 지점을 방문한다.
n,m = map(int,input().split())
matrix = [[0,0,1,1,0],[0,0,0,1,1],[1,1,1,1,1],[0,0,0,0,0]]
def iswall(x,y):
    if matrix[x][y] ==1:
        return False
    if x<0 or y<0:
        return False
    if x<n or y<m :
        return False
    return True
def dfs(x,y):
    if matrix[x][y]==0:
        matrix[x][y]=1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x + 1, y)
        dfs(x , y+1)
        return True
    return False

result = 0
for i in range(4):
    for j in range(5):
        if dfs(i,j) == True:
            result+=1
print(result)
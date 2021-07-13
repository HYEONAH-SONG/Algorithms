# 행렬의 가로줄의 갯수 rows
# 행렬의 세로줄 갯수 cols
# 스와이프 행위의 방향과 범위를 나타내는 수들의 목록 swipes
# 사라졌다가 다시 행렬에 채워지는 숫자들의 합을 return

def one(r1,c1,r2,r3):
    for i in
def two(r1, c1, r2, r3):
def three(r1, c1, r2, r3):
def four(r1, c1, r2, r3):



def solution(rows, columns,swipes):
    array = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
    for i in swipes:
        if i[0] == 1:
            one(r1, c1, r2, r3)


rows, columns = 4,3
swipes = [[1,1,2,4,3],[3,2,1,2,3],[4,1,1,4,3],[2,2,1,3,3]] # d번 방향으로 r1,c1부터 r2,c2까지 모든 숫자들을 스와프
print(solution(rows, columns,swipes))

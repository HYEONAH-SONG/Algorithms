# 2차원 배열 구조를 만들기 위한 행, 열 정보를 콤마(,)로 구분해 입력
table = input()
l = list(map(int, table.split(', ')))
l3=[]
row = int(l[0])
col = int(l[1])

for i in range(row) :
    l2 =[] # 새로운 행
    for j in range(col) :
        l2.append(i*j)
    l3.append(l2)

print(l3)
import sys
sys.stdin = open("input.txt")

T = int(input()) #테스트 케이스의 개수
result = [] # 매번 테스트 케이스 마다 결과 작성
kind = ["Yonsei","Korea","Draw"] # 나올수 있는 결과의 종류
for _ in range(T): #test case 갯수
    Y = 0
    K = 0
    for _ in range(9):
        s1,s2 = map(int, input().split(" "))
        Y +=s1
        K +=s2

    if Y> K:
         result.append(kind[0])
    elif Y < K:
         result.append(kind[1])
    else:
         result.append(kind[2])

for i in range(len(result)):
    print(result[i])

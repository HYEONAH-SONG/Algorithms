import sys
sys.stdin = open("sample_input.txt")

# 각 변에는 동일하 개수의 숫자
# 시계 방향 순으로 높은 자리 숫자 => 한 칸씩 회전
def calculate(N, K, W):
    # 보물상자에 적힌 숫자로 만들 수 있는 모든 수를 구해야 한다.
    l = []
    count = N//4
    for j in range(count):
        for i in range(j,N,count): # 0,3,6,9
            l.append(W[i:i+count])
    l = list(set(l)) # 중복제거
    l = sorted(l,reverse=True)
    #print(l)
    return int(l[K-1],16)

case = int(input())
for i in range(case):
    N, K = map(int,input().split()) # 글자의 크기 / K번째 큰 수
    W = input() * 2
    #print(N, K, W)
    result = calculate(N, K, W)
    print("#{} {}".format(i+1,result))
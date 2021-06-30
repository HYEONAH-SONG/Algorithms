# 길이가 같은 두 1차원 정수 배열 a,b의 내적을 return 하도록 함수를 구현
# 내적 : a[0]*b[0] + a[1]*b[1] + ... + a[n-1]*b[n-1]
# 길이는 1,000 이하 -> for문 하나만 이용

def solution(a, b):
    result = 0
    for i in range(0,len(a)):
        result += a[i]*b[i]
    return result

a = [1,2,3,4]
b = [-3,-1,0,2]
print(solution(a,b))
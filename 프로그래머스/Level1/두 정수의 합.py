# 두 정수가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수

def solution(a, b):
    answer = 0
    if a < b:
        for i in range(a,b+1):
            answer +=i
    else:
        for i in range(b,a+1):
            answer +=i
    return answer

def adder(a, b):
    # 함수를 완성하세요
    if a > b: a, b = b, a
    return sum(range(a,b+1))

def adder(a, b):
    return (abs(a-b)+1)*(a+b)//2

a,b = 3,5
print(solution(a,b))
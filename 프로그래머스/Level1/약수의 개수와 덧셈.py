# 1 ≤ left ≤ right ≤ 1,000 ---> O(N^2) 까지 가능
# 약수의 갯수가 짝수인 수는 더함
# 약수의 갯수가 홀수인 수는 뺌
# list comprehension을 활용

def solution(left, right):
    answer = 0
    for num in range(left, right + 1): # left ~ right
        operator = 1
        divison = len([n for n in range(1, num + 1) if num % n == 0]) # 약수의 갯수 구하기
        if divison % 2 == 1: # 수개 인 경우
            operator = -1
        answer += num * operator
    return answer
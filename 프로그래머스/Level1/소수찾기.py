import math

# 제곱근까지만 보고 소수를 판별하는 함수
def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x))+1):
    # x가 해당 수로 나누어 떨어진다면
        if x % i == 0:
            return False
    return True

def solution(n):
    count = 0
    for i in range(2,n+1):
        if is_prime_number(i) == True:
            count +=1
    return count
n = 5
print(solution(n))


# dynamic programming --> 값들을 "저장"해두고 필요할 때 꺼내 쓴다.
# 피보나치 수열 정리 ★★★★
# 경우의 수 많은 경우 ---> dp 무조건 100% 활용하기
#  bottom up 을
def solution(n):
    answer = [0, 1]  # F(0)=0, F(1)=1
    for i in range(2, n + 1):  # F(n) = (F(n-1) + F(n-2)) % 1234567
        answer.append((answer[i - 1] + answer[i - 2]) % 1234567)
    return answer[-1]  # 마지막 결과를 return
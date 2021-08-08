# 사용할 수 있는 정사각형의 갯수 구하기
# 문제의 창의적인 해결 능력을 보는 문제
# 한 점이라도 제대로 찍힌 경우에는 사각형 1개 / 아닌 경우 2개
# 참고 : https://leedakyeong.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%A9%80%EC%A9%A1%ED%95%9C-%EC%82%AC%EA%B0%81%ED%98%95-in-python
import math
# def solution(w,h):
#     return w*h - (w+h-math.gcd(w,h))

def gcd(a, b):
    while b != 0:
        n = a % b
        a = b
        b = n
    return a

def solution(w,h):
    g = gcd(w, h)
    answer = w * h - w - h + g

    return answer

w, h = 8,12
print(solution(w,h))
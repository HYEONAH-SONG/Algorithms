# 사용할 수 있는 정사각형의 갯수 구하기
# 문제의 창의적인 해결 능력을 보는 문제
# 한 점이라도 제대로 찍힌 경우에는 사각형 1개 / 아닌 경우 2개

import math
def solution(w,h):
    return w*h - (w+h-math.gcd(w,h))


w, h = 8,12
print(solution(w,h))
# 2. 원의 면적을 계산하는 함수 calcArea(radius)을 정의하시오. 만약 원의 반지름이 주어지지 않았으면 5.0으로 간주한다. 즉, 함수의 ”디폴트 인수“를 사용하시오. [10]
import math
def calArea(radius =5.0):
    area = radius * radius * math.pi
    return area
print(calArea(6))
print(calArea())
#사용자로부터 콤마(,)로 구분해 여러 원의 반지름을 입력 받아
#이들에 대한 원의 둘레를 계산

import math
str = input()

l = str.split(',') # 콤마로 문자열 분리
new = [map(int,l)]
for key in l:
        key = int(key)
        key = round(2 * key * math.pi,2)
        new.append(key)
        print(key, end=', ')




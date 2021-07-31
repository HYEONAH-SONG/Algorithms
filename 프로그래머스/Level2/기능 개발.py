# 각 기능 --> 100 % 이면 서비스에 반영이 가능함
import math
from collections import deque

def solution(progresses, speeds):
    stack = deque()
    answer = [1]

    # 걸리는 날짜 구하기(Days)
    for progress, speed in zip(progresses,speeds):
        stack.append(math.ceil((100 - progress)/speed))

    origin = stack.popleft()
    for index, day in enumerate(stack):
        if day <= origin:
            answer[-1] += 1
        else:
            origin = day
            answer.append(1)
    return answer

progresses, speeds =[93, 30, 55],[1, 30, 5]
print(solution(progresses, speeds))

# 7,3,9
# 1. 각각의 작업 Day를 구한다.
# 2. 만약 다음 Day가 이전의 Day보다 작은 경우에는 Count + 1을 해준다.
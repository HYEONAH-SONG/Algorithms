# 배열 arr에서 연속적으로 나타나는 숫자(중복 숫자)는 하나만 남기고 전부 제거
from collections import deque
def solution(arr):
    arr = deque(arr)
    answer = [arr.popleft()]
    for _ in range(len(arr)):
        num = arr.popleft()
        if answer[-1] == num:
            continue
        else :
            answer.append(num)
    return answer

arr = [1,1,3,3,0,1,1]
print(solution(arr))
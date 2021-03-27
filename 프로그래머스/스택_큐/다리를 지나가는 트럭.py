#모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는가
from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    stack = deque([0]*bridge_length) # 다리를 건너는 트럭들
    dq=deque(truck_weights) # 대기 트럭
    sum_n = 0
    while dq or sum_n:
        answer+=1
        sub =stack.popleft()
        sum_n -= sub
        if dq : # 대기 트럭이 사라질 때 까지
            if  sum_n + dq[0] <= weight: # 다리에 다른 트럭이 올 수 있는 경우
                stack.append(dq.popleft())
                sum_n +=stack[-1]
            else:
                stack.append(0)
    return answer

print(solution(2,10,[7,4,5,6]))
#모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는가
from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    stack = [0] * bridge_length # 다리를 건너는 트럭들
    dq=deque(truck_weights) # 대기 트럭
    while stack:
        answer+=1
        stack.pop()
        if dq : # 대기 트럭이 사라질 때 까지
            if  sum(stack) + dq[0] <= weight: # 다리에 다른 트럭이 올 수 있는 경우
                stack.append(dq.popleft())
            else:
                stack.append(0)
    return answer

print(solution(2,10,[7,4,5,6]))
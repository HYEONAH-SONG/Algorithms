#모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는가
from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0 # 다리 건너는데 걸리는 시간
    stack =[]
    dq = deque(truck_weights)
    while stack or dq :
        if sum(stack) <= weight and dq:
            stack.append(dq.popleft())
            answer +=bridge_length
        else :
            stack.pop()
    return answer


bridge_length =100
weight = 100
truck_weights = [10]
print(solution(bridge_length, weight, truck_weights))
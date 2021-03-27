# 1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
# 2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
# 3. 그렇지 않으면 J를 인쇄합니다.
from collections import deque
def solution(priorities, location):
    answer = 0 # 내가 인쇄를 요청한 문서가 몇 번째로 인쇄되는지에 대한 횟수
    dq = deque([[v,i] for i,v in enumerate(priorities)])
    while dq:
        cur = dq.popleft()
        if cur[0] < max(dq)[0]:
            dq.append(cur)
        else:
            answer+=1
            if cur[1]==location:
                break
    return answer


priorities = [1, 1, 9, 1, 1, 1]
location = 0
print(solution(priorities,location))


T = [73,74,75,71,69,72,76,73]
day_list =[]
for index, value in enumerate(T):
    count = []
    for i in range(index+1,len(T)-1):
        count.append(T[i])
        if value >= T[i]:
            continue
        else:
            break
    day_list.append(len(count))
print(day_list)


def dailyTemporatures(T):
    answer = [0] * len(T)
    stack =[]
    for index,cur_value in enumerate(T):
        # 현재 온도가 스택 값보다 높다면 정답 처리
        while stack and cur_value >T[stack[-1]]:
            last = stack.pop()
            answer[last] = index-last
        stack.append(index)

    return answer

print(dailyTemporatures(T))
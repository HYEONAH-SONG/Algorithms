T = [73,74,75,71,69,72,76,73]
day =[0]*len(T)
stack= []
for index,value in enumerate(T):
    # 현재의 온도가 스택 값보다 높다면 정답 처리
    while stack and T[stack[-1]]<value:
        i = stack.pop()
        day[i] = index-i
    stack.append(index)
    # stack에 index 쌓아두기
    # 핵심은 온도가 떨어지면 stack에 저장하고
    # 온도가 상승하면 해당 인댁스를 빼기
    # 0 --> 1 --> 2 ---> 2, 3, 4 --> 2,5 ---> 2,5,6
print(day)
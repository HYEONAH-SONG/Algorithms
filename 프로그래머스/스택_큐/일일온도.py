T = [73,74,75,71,69,72,76,73]

def daily(T):
    stack=[]
    answer=[0]*len(T)
    for i, value in enumerate(T):
        while stack and value>T[stack[-1]]:
            last=stack.pop()
            answer[last]=i-last
        stack.append(i)
    return answer

print(daily(T))

T = [73,74,75,71,69,72,76,73]
day =[]
stack= []
for index,value in enumerate(T):
    while stack and T[stack[-1]]<value:
        i = stack.pop()
        day.append(index-i)
    stack.append(index)

print(day)
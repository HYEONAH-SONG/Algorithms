T = [73,74,75,71,69,72,76,73]
day_list =[]
for index, value in enumerate(T):
    count = []
    for i in range(index+1,len(T)):
        count.append(T[i])
        if value >= T[i]:
            continue
        else:
            break
    day_list.append(len(count))
print(day_list)
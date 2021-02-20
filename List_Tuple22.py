l = [5, 6, 77, 45, 22, 12, 24]

t = [i for i in l if not (i % 2 ==1)]
result = [i for i in l if i not in t]
print(result)
num = input()
l = list(map(int,num.split(', ')))

result = [i for i in l if i & 1]
result_n = ', '.join(map(str, result))
print(result_n)
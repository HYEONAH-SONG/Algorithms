# 정수 N을 입력받아서 1부터 N 까지의 정소를 키로 하고 그 정수의 제곱을 값으로 하는 딕셔너리

num = int(input())
dic = {}
for key in range(1, num+1) :
    dic[key] = key**2
print(dic)
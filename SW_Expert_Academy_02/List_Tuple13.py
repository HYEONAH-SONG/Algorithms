# 사용자가 숫자를 입력하면 숫자의 각 자릿수의 합을 구해서 반환하는 프로그램을 작성
num = input()
num = list(num)
sum = 0

for key in num :
    sum = sum + int(key)
print(sum)
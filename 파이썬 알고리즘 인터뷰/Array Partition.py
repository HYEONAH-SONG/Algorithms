# n개의 페어를 이용한 min(a,b)의 합으로 만들 수 있는 가장 큰 수를 출력한다.

array = [1,4,3,2] #1,2,3,4,5
# 1,2 / 1,3 / 1,4 /2,3 / 2,4,/ 3,4
array = sorted(array) # 배열 정렬하기
# 배열이 항상 짝수의 갯수로 입력을 받을 것이다.
sum = 0
for i, value in enumerate(array):
    if i % 2 == 0 :
        sum+= value
print(sum)

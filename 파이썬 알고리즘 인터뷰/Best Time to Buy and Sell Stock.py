# 한번의 거래로 낼 수 있는 최대의 이익을 산출하라
# 최대 이익은 최대값 - 최솟값
arr = [7,1,5,3,6,4]
max_price=[]
price = 0
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        price = arr[j]-arr[i]
        max_price.append(price)
print(max(max_price))
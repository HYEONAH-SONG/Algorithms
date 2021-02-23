# 피보나치 수열을 수행하시오
# 피보나치 수열이란 앞의 두 수의 합이 바로 뒤의 소가 되는 수의 배열을 의미한다


def fibo(num) :
    fibo_list =[1,1]
    sum = 0
    for cnt in range(num-2) :
        sum = fibo_list[-1] + fibo_list[-2]
        fibo_list.append(sum)
    return fibo_list


num = int(input())
print(fibo(num))


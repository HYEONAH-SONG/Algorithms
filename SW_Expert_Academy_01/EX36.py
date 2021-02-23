# 소수인지를 판단하는 프로그램

def prime(num) :
    for div in range(2,num) :
        if num % div == 0:
            print("소수가 아닙니다.")
            break
        elif div == num -1:
            print("소수입니다.")
        else:
            continue

number = int(input())
prime(number)
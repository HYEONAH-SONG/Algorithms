# 주어진 정수가 소수인지를 검사하는 함수 testPrime(n)을 작성하고, 이 함수를 호출하여서 2부터 100 사이의 소수를 출력하시오. [10]

def testPrime(n):
    answer = []
    for i in range(2,n+1):
        count = 0
        for j in range(1,i):
            if i % j == 0 :
                count+=1
        if count == 1:
            answer.append(i)
    return answer
print(testPrime(100))



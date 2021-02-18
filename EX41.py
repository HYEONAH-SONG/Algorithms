#다음과 같이 팩토리얼을 구하는 함수를 정의해 입력된 숫자에 대한
#팩토리얼 값을 구하는 프로그램을 작성하십시오.


def factor(number) :
    total = 1
    for i in range(1, number +1) :
        total = total * i
    print(total)



num = input()
factor(int(num))
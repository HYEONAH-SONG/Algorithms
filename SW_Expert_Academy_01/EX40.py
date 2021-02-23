#숫자에 대해 제곱을 구하는 함수를 정의히고, 다음과 같이 숫자를 콤마(,)로 구분해 입력하면
#정의한 함수를 이용해 제곱 값을 출력하는 프로그램을 작성하십시오.

def square(num1, num2):
    num11 = pow(num1,2)
    num22 = pow(num2,2)
    print("square("+str(num1)+") =>",num11)
    print("square("+str(num2)+") =>",num22)


num = input()
num_1 = num.split(', ')[0]
num_2 = num.split(', ')[1]

square(int(num_1), int(num_2))
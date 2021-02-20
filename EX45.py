from datetime import datetime

def calculate(name, age) :
    year = 100- age + datetime.today().year
    print(name+"(은)는"+ str(year) +"년에 100세가 될 것입니다.")


name = input()
age = int(input())
calculate(name, age)
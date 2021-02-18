from datetime import datetime

def calculate(name, age) :
    year = 100-datetime.today().year
    print(name+"(은)는"+datetime.today().year  "년에 100세가 될 것입니다.")


name = input()
age = int(input())

# 주급 계산하기
# 사용자에게 근무시간과 시간당 임금을 물어본다.
# 주당 근무 시간이 40시간을 넘으면 40시간이 넘는 노동에 대해 1.5배의 임금을 지불해야 한다.
# 이번 주에 받는 총 임금을 계산하는 프로그램을 작성하시오.

def cal_total_wage(time,wage):
    total = 0
    if time > 40:
        total = wage * 40 + (time - 40) * wage * 1.5
    else:
        total = wage * time
    return  total


time = int(input('근무시간을 입력하시오 :'))
wage = int(input('시간당 임금을 입력하시오 :'))

print('총임금은 {}'.format(cal_total_wage(time,wage)))
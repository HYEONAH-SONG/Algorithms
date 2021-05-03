# 5:12
# 같은 순위를 가질 수 없다
# + - *
# 계산된 결과가 음수라면 절대값으로 변환하여 제출한다
# 피연산자는 0 이상 999 이하
# 같은 연산자끼리는 앞에 있는 것의 우선 순위가 더 높다
def solution(expression):
    # answer = 0
    cal_list = expression.split('-')
    for i in cal_list:
        if '+' in i:
            new = i.split('+')
            print(new)


    # answer = max(abs(cal_list))
    # return answer

expression = "100-200*300-500+20"
print(solution(expression))

#피연산자의 리스트와 오퍼레이션 리스트를 분리한다
# 100,200,300,500,20
# -,*,-,+
#
# 1. - * +  >>  우선 순위를 기준으로 양 옆의 피연산자를 계산한다.
# 2. - + *
# 3. + - *
# 4 + * -
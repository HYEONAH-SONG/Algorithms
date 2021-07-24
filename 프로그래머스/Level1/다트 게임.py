# 다트 던지는 횟수 : 3회
# 한 번에 얻을 수 있는 점수 : 0 ~ 10
# S = 1제곱, D = 2제곱, T = 3제곱
# * = (해당 점수 + 바로 이전의 점수)2배수
# # = - 해당 점수

def solution(dartResult):
    score = []
    num = 0
    for i in dartResult:
        # 숫자인 경우
        if i.isnumeric():
            num = num*10 + int(i) # 10인 경우 고려함
            print(num)
        elif i == 'S':
            score.append(num)
            num = 0
        elif i == 'D':
            score.append(num ** 2)
            num = 0
        elif i == 'T':
            score.append(num**3)
            num = 0
        elif i == '*':
            if len(score) > 1: # 첫 번째 기회가 아닌 경우
                score[-2] = score[-2] * 2
                score[-1] = score[-1] * 2
            else: # 첫번째 기회인 경우
                score[-1] = score[-1] * 2
        else: # '#'인 경우
            score[-1] = score[-1] * -1
    return sum(score)

print(solution('1D2S#10S'))
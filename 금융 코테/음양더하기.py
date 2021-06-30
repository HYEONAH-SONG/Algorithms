# 정수들의 절대값을 차례대로 담은 정수 배열 absolute와 이 정수들의 부호를 차례대로 담은 불리언 배열 signs가 매개변수로 지어진다.
# 실제 정수들의 합을 구하여 return 한다.
# 배열이 1,000 이하 --> for 문 하나를 사용
def solution(absolutes, signs):
    answer = 0
    for i in range(0,len(absolutes)):
        if signs[i]==True:
            answer += absolutes[i]
        else:
            answer += absolutes[i] * -1
    return answer

absolutes=[1,2,3]
signs=['false','false','true']
print(solution(absolutes,signs))
# 그리디 알고리즘
# key point : "중복이 없다" "여벌의 체육복이 있는 학생도 도난 당했을 수 있다."
# 중복 제거할 때 : set을 이용하면 편리함
# list와 set은 다른 서로 다른 타입이다 --> 선언할 때 다른 이름으로 정의해야 함

# 학생들의 번호는 체격순
# 바로 앞 번호의 학생이나 바로 뒷 번호의 학생에게만 체육복을 빌려줄 수 있음
# 최대한 많은 학생이 체육복 소지해야함

def solution(n, lost, reserve):
    reserve_set = set(reserve).difference(set(lost))
    lost_set = set(lost).difference(set(reserve))
    # reserve에서 이전의 인덱스부터 확인해야한다
    for i in reserve_set:
        if i-1 in lost_set :
            lost_set.remove(i-1)
        elif i+1 in lost_set:
            lost_set.remove(i+1)
    answer = n - len(lost_set)
    return answer

n = 5
lost = [5]
reserve = [5]
print(solution(n,lost,reserve))
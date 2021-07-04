# 그리디 알고리즘
# key point : "중복이 없다" "여벌의 체육복이 있는 학생도 도난 당했을 수 있다."
# 중복 제거할 때 : set을 이용하면 편리함
# list와 set은 다른 서로 다른 타입이다 --> 선언할 때 다른 이름으로 정의해야 함

# 학생들의 번호는 체격순
# 바로 앞 번호의 학생이나 바로 뒷 번호의 학생에게만 체육복을 빌려줄 수 있음
# 최대한 많은 학생이 체육복 소지해야함

# def solution(n, lost, reserve):
#     reserve_set = set(reserve).difference(set(lost))
#     lost_set = set(lost).difference(set(reserve))
#     # reserve에서 이전의 인덱스부터 확인해야한다
#     for i in reserve_set:
#         if i-1 in lost_set :
#             lost_set.remove(i-1)
#         elif i+1 in lost_set:
#             lost_set.remove(i+1)
#     answer = n - len(lost_set)
#     return answer

def solution(n, lost, reserve):
    student = [1 for _ in range(n+2)]
    cnt = 0
    for i in lost:
        student[i]-=1
    for i in reserve:
        student[i]+=1
    # print(student)
    for index in range(1,n+1):
        if student[index] == 0 and student[index+1]==2:
            student[index],student[index+1]=1,1
        elif student[index] == 0 and student[index-1]==2:
            student[index],student[index-1]=1,1
        # print(student)
        # print(index,student[index])
    for i in student[1:n+1]:
        if i != 0 :
            cnt +=1
    return cnt

n = 5
lost = [2, 4]
reserve = [1, 3, 5]
print(solution(n,lost,reserve))
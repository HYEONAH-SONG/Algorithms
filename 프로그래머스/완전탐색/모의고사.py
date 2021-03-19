# 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.
# 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
# 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
# 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...


def solution(answers):
    student1 =[1,2,3,4,5] #5
    student2 = [2, 1, 2, 3, 2, 4, 2, 5] #8
    student3 =[3, 3, 1, 1, 2, 2, 4, 4, 5, 5] #10
    array = [0,0,0]
    answer = []
    for index, value in enumerate(answers):
        if value == student1[index%5]:
            array[0] +=1
        if value == student2[index%8]:
            array[1] +=1
        if value == student3[index%10]:
            array[2] +=1

    num = max(array)
    for index, value in enumerate(array) :
        if num == value :
            answer.append(index+1)
    return answer


answers =[1,3,2,4,2]
print(solution(answers))
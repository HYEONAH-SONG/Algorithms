# 배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하려 합니다.

def solution(array, commands):
    answer = []
    for i in commands:
        first,end,num = i[0]-1,i[1],i[2]-1
        arr = sorted(array[first:end])
        answer.append(arr[num])
    return answer

array=[1, 5, 2, 6, 3, 7, 4]
commands=[[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array,commands))
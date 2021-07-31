
import itertools
# def solution(numbers):
#     array = []
#     num = list(itertools.permutations(numbers)) # 3개의 원소로 수열 만들기 ---> 시간 복잡도 초과
#     for i in num:
#         array.append(str(i[0])+str(i[1])+str(i[2]))
#     return str(max(array))


def solution(num):
    num =[str(num) for num in numbers]
    num.sort(key = lambda x : x*3, reverse = True)
    return str(int(''.join(num)))

numbers = [6, 10, 2]
print(solution(numbers))


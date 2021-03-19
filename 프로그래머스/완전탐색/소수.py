from itertools import permutations

def solution(numbers):
    array =[]
    n_list = []
    count_sum = 0
#   numbers = [int(i) for i in numbers]
    for i in range(1,len(numbers)+1):
        number = permutations(numbers,i)
        n_list = set(number)
        for j in n_list:
            str="".join(j)
            array.append(int(str))
    array = list(set(array))
    print(array)
    # num = [int(i) for i in n_list]
    # print(num)
    # 문자열 속의 숫자들의 조합 리스트

    for key in array :
        count = 0
        for division in range(2, key):
            if key % division == 0:
                count+=1
                break
        if key >1 and count == 0 :
            count_sum +=1
    return count_sum

numbers ="011"
print(solution(numbers))
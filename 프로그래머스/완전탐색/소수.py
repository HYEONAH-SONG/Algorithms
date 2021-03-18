def solution(numbers):
    n_list = []
    count_sum = 0
    for i in range(len(numbers)):
        n_list.append(numbers[i])
        for j in range(len(numbers)):
            if i != j :
                n_list.append(numbers[i] + numbers[j])
    num = [int(i) for i in n_list]

    for key in list(set(num)) :
        count = 0
        for division in range(2, key):
            if key % division == 0:
                count+=1
                break
        if key > 1 and count == 0 :
            count_sum +=1
    return count_sum

numbers ="011"
print(solution(numbers))
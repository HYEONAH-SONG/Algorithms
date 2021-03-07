#리스트의 항목 중 유일한 값으로만 구성된 리스트를 반환하는 함수를 정의하고
#이 함수를 이용해 리스트의 중복 항목을 제거하는 프로그램을 작성하십시오.
#EX38
def no_dupli(list) :
    list2 = []
    for key in list :
        if key not in list2:
            list2.append(key)
        else :
            continue
    return list2

list = [1, 2, 3, 4, 3, 2, 1]
print(list)
list = no_dupli(list)
print(list)
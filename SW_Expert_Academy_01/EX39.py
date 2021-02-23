#정렬된 숫자를 가진 리스트에서 특정 숫자를 찾는 함수를 정의하고,
#이 함수를 이용해 임의의 숫자의 포함 여부를 출력하는 프로그램을 작성하십시오.

list = [2, 4, 6, 8, 10]

def find(element) :
    for key in list:
        if element == key :
            print(str(element) +" => True")
            break
        elif (element != key) and (key == list[-1]):
            print(str(element) +" => False ")
        else :
            continue
print(list)
find(5)
find(10)
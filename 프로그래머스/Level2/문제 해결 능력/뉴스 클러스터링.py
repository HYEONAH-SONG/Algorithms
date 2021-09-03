
def convert(str1, str2):
    list1 = []
    list2 = []
    for i in range(0,len(str1)-1):
        list1.append(str1[i:i+2])
    for i in range(0,len(str2)-1):
        list2.append(str2[i:i+2])

    list1 = [i.lower() for i in list1 if i.isalpha()]
    list2 = [i.lower() for i in list2 if i.isalpha()]
    print(list1, list2)
    return list1,list2

def calculate(list1, list2):

    # A와 B가 공집합인 경우
    if not list1 and not list2:
        return 1

    # 중복되는 원소가 없는 경우
    elif len(list1) == len(set(list1)) and len(list2) == len(set(list2)):
        result1 = len(list(set(list1) & set(list2)))
        result2 = len(list(set(list1)|set(list2)))
        return result1 / result2

    # 중복되는 원소가 있는 경우
    else:
        dict1,dict2 = {},{}
        result1 = list(set(list1) & set(list2)) # 곱 원소 (only 1개)
        result2 = list(set(list1)|set(list2)) # 합 원소 (only 1개)
        len1 = len(result1)
        len2 = len(result2)

        for i in list1:
            if i in dict1:
                dict1[i] +=1
            else:
                dict1[i] = 1

        for i in list2:
            if i in dict2:
                dict2[i] +=1
            else:
                dict2[i] = 1

        for i in result1:
            if dict1[i]>1 or dict2[i]>1:
                len1 += min(dict1[i],dict2[i])-1
                continue

        for i in result2:
            if (i in list1) and (i not in list2):
                len2 += dict1[i]- 1
                continue
            elif (i in list2) and (i not in list1):
                len2 += dict2[i]- 1
                continue
            elif (i in list2) and (i in list1):
                len2 += max(dict1[i], dict2[i])-1
                continue
        return len1 / len2

def solution(str1, str2):
    list1,list2 = convert(str1, str2)
    similarity = calculate(list1,list2)
    return int(65536 * similarity)
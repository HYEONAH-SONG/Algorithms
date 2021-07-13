# s의 변형 문자열 : s의 모든 글자들 사이에 공백을 동일한 길이로 삽입해서 만들어지는 문자열
# line1 안에 들어있는 line2의 변형 문자열 개수를 return
# b,b,b --> 0,1,2
# b, ,b, ,b --> 0,2,4
# b, , , b, , ,b --> 0,3,6
# b, , , b, , ,b --> 0,4,8
import re
def solution(line1, line2):
    count = 0
    blank = 1
    c=0
    # if line2 in line1:
    #     count += line1.count(line2)
    new_list = list(line2)
    new_list2 = list(line1)
    for i in range(len(line1)): # 시작점
        for j in range(len(line2)):
            if new_list2[i:(i+len(line2))*blank:blank] == new_list[j]:
                print("yrdy")
                c +=1
    if c == 3:
        count +=1
    blank +=1
    return count

line1, line2 = "abbbcbbb","bbb"
print(solution(line1,line2))




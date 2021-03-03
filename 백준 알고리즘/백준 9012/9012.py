import sys
sys.stdin = open("input.txt")

T = int(input()) #테스트 케이스의 개수

# for _ in range(T) :
#     str = input()
#     cnt = 0
#     isTrue="NO"
#     if str.count("(") == str.count(")") and str[-1] == ")" and str[0] == "(":
#         for i in range(len(str)-1):
#             if str[i] == "(" :
#                 cnt +=1
#             else :
#                 cnt -=1
#         if cnt >=0:
#             isTrue = "YES"
#     print(isTrue)

for _ in range(T) :
    l_list =[]
    str = input()
    isTrue = "NO"
    for i in range(len(str)):
        if str[i]=="(":
            l_list.append(str[i])
        elif str[i]==")" and l_list:
            l_list.pop()
        else:
            break
    else:
        if not l_list:
            isTrue = "YES"
    print(isTrue)
# 시간복잡도 : 이중 for문을 사용하면서 .count() 함수를 사용하기 때문에 O(n^2) + O(n) = n^2 이 된다.
# 시작과 끝은 ()이고, 절대로 이전의 문자열에서 )의 갯수가 더 많아서는 안된다
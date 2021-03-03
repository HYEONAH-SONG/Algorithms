import sys
sys.stdin = open("input.txt")

T = int(input()) #테스트 케이스의 개수

for i in range(T):
    str = input()
    n_list=[]
    isCorrect = True
    dict1 = {"S":13,"D":13,"H":13,"C":13}
    for j in range(0,len(str),3):

        if str[j:j+3] not in n_list:
            n_list.append(str[j:j + 3])
            dict1[str[j]]-=1
        else:
            isCorrect = False
            break
    if isCorrect : print("#{} {} {} {} {}".format(i + 1, dict1["S"], dict1["D"], dict1["H"], dict1["C"]))
    else: print("#{} ERROR".format(i + 1))
# A 는 1, J,Q,K는 11,12,13
# 카드 무늬 S, D, H, C
# 카드 숫자 01 ~ 13

# 문자열을 3개의 문자씩 나누기
# 중복을 확인하기
# 각 무늬별 갯수 구하기

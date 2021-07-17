# 문자열의 길이 : 4 or 6
# 숫자로만 구성
# isdigit() : 문자열이 숫자로 구성되어있는지 판별해주는 함수 ---> 문자열이 하나라도 포함된 경우에는 False 리턴


def solution(s):
    answer = True
    if (len(s) == 4 or len(s)==6) and s.isdigit()==True:
        return True
    else:
        return False
s = "a234"
print(solution(s))
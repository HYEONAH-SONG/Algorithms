# s의 변형 문자열 : s의 모든 글자들 사이에 공백을 동일한 길이로 삽입해서 만들어지는 문자열
# line1 안에 들어있는 line2의 변형 문자열 개수를 return
# b,b,b --> 0,1,2
# b, ,b, ,b --> 0,2,4
# b, , , b, , ,b --> 0,3,6
# b, , , b, , ,b --> 0,4,8
# 인덱스 슬라이씽
def solution(line1, line2):
    count = 0
    blank = 1
    i =0
    stack =""
    # 한 간격에 도는 알고리즘
    for i, value in enumerate(line1):
        if value == line2[0]:
            for j in range(i,len(line1),blank):
                if len(stack) < len(line2):
                    stack+=line1[j]
                elif stack == line2 and len(stack)==len(line2):
                    count +=1
                    stack = []
                    continue
                else:
                    stack = []
                    continue


    print(stack.count(line2))
    print(stack)
    print("count:",count)


line1, line2 = "abbbcbbb","bbb"
print(solution(line1, line2))




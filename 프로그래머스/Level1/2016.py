# 2016년 1월 1일은 금요일
# 2016년 a월 b일은 무슨 요일일까요?
# 윤년 : 2월 29일 존재

def solution(a, b):
    date = b
    day = ["THU","FRI","SAT","SUN","MON","TUE","WED"]
    month = [31, 29, 31, 30, 31, 30 , 31, 31, 30, 31, 30, 31]
    for i in range(0,a-1):
        date += month[i]
    return day[date%7]

a, b = 5,24
print(solution(a,b))
# 아무 것도 입력하지 않고 엔터만 입력하면 입력이 종료
# 여러 문장을 입력받아 대문자로 변환해 출력하는 프로그램을 작성
count = 1
while count <4 :
    str_ = input()
    if not str_:
        break
    print(">> {}".format(str_.upper()))
    count =count +1
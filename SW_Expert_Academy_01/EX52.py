#'abcdef' 문자열의 각각의 문자를 키로 하고 0~5 사이의 정수를 값으로 하는 딕셔너리 객체를 생성하고,
# 이 딕셔너리 객체의 키와 값 정보를 출력하는 프로그램을 작성

data = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5}
for key in data:
    print(key + ": " +str(data.get(key)))
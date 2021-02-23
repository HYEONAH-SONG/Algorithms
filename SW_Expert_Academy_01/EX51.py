#가변형 인자를 전달 받아 가장 큰 값을 반환하는 함수를 정의

def maximum(*args) :
    print("max"+str(args),"=> "+ str(max(args)))



maximum(3, 5, 4, 1, 8, 10, 2)
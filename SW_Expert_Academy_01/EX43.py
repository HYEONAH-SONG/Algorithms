'''
인자로 전달된 숫자를 이용해 카운트다운하는 함수 countdown을 정의하고,
이 함수를 이용하여 countdown(0), countdown(10)을 순서대로 실행하십시오.
0보다 작거나 같은 인자가 전달되었을 경우 "카운트다운을 하려면 0보다 큰 입력이 필요합니다."를 출력하십시오.
'''

def countdown(count) :
    if count <= 0 :
        print ("카운트다운을 하려면 0보다 큰 입력이 필요합니다")
    else :
        while count > 0 :
            print(count)
            count -=1
countdown(0)
countdown(10)

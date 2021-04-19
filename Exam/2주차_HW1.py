# 카운트 다운 프로그램
# 로켓을 발사하기 위하여 카운트 다운을 하는 프로그램
import time

def rocket(count):
    while count > 0:
        print(count,end=' ')
        count -= 1
        time.sleep(1)
    time.sleep(1)
    print('발사')


count = int(input('숫자를 입력하시오: '))
rocket(count)
# 소유 가정 금액 : m의 백의 자리 미만은 버림을 하고 계산
# 어떤 시민의 소유 가정 금액이 threshold 미만인 경우에는 세금을 걷지 x
# 어떤 시민의 소유 가정 금액이 threshold 이상인 경우에는 ranksize 단위만큼 1%의 세율이 추가적으로 붙는다
# 세금은 maxratio 이상으로 높은 세율을 적용하지 않는다.
import math
def solution(money,minratio,maxratio,ranksize,threshold,months):
    month = 1 # 진행하는 달
    size = minratio
    while month <= months:
        m = (money // 100) * 100  # 소유 가정 금액
        if m < threshold :
            return money
        else : # 소유 가정 금액이 thread 이상인 경우
            size = minratio + (m-threshold)//ranksize
            if size > maxratio:
                size = maxratio
            money = money - int(m *(size/100))
        month +=1
    return money


# 초기 소유 금액, 세금 정책 파라미터, 정책 시뮬레이션 매개변수
# money,minratio,maxratio,ranksize,threshold,months = 12345678,10,20,250000,10000000,4
money,minratio,maxratio,ranksize,threshold,months = 123456789,0,0,1,0,360
print(solution(money,minratio,maxratio,ranksize,threshold,months))
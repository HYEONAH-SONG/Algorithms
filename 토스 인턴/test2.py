# 가능하면 적은 양의 음식을 골라야 한다.

snack = {"콜라":[300,10],"초콜릿":[130,30],"과자":[120,20],"젤리":[20,30]}
def solution(seconds):
    count = 0 # 고른 음식의 갯수
    for i in snack:
        while(seconds >= snack[i][0] and snack[i][1] > 0):
            seconds -= snack[i][0]
            snack[i][1] = snack[i][1]-1
            count += 1
    return count

print(solution(460))

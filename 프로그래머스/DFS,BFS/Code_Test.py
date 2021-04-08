# 받을 수 있는 상품 번호가 적혀있는 상품권을 사람들이 각자 하나씩 들고있다.
# 다른 사람과 교환이 가능하다
# 원하지 않는 상품을 받는 사람의 수를 최소화 해야한다.


def git_card(gift_cards, wants):
    dic = {}
    result = len(wants)
    for thing in wants:
        if thing not in dic:
            dic[thing] = 1
        else :
            dic[thing]= dic[thing] +1
    for key in gift_cards:
        if key in dic.keys() and dic[key]>0:
            dic[key] -= 1
            result -=1
        else:
            continue
    return result

git_cards = [4,5,3,2,1]
wants = [2,4,4,5,1]

print(git_card(git_cards,wants))
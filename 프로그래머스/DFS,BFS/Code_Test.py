# 받을 수 있는 상품 번호가 적혀있는 상품권을 사람들이 각자 하나씩 들고있다.
# 다른 사람과 교환이 가능하다
# 원하지 않는 상품을 받는 사람의 수를 최소화 해야한다.

# 1. 처음에 시간복잡도 제한사항 :  gift_card랑 want의 길이가 100000 이하 -->이중 for문은 무조건 쓰면 안되겠다!
# 2. 원하는 상품을 받는 사람의 조건으로 result를 구하려고 하니까 n^2의 시간 복잡도가 나오게 된다 --> 원하는 상품을 받지 않을 조건을 구해보자
# 순서에 관계없이 두 개의 리스트를 비교했을 때 원소의 갯수가 같다면 매칭이 된다. ex) git_card, want 에 5와 1이 1개씩 존재하므로 이 원소들은 원하는 사람에게 성공적으로 전달이 된다
# 원소의 갯수가 다르다면 원치않는 선물을 받는 사람이 있다는 의미
# 결국 초점을 둬야 하는 것은 want의 리스트이다. 따라서 want의 상품번호 갯수를 딕셔너리로 표현하자 (시간 복잡도 1이기 때문)
# 원하지 않는 상품을 받는다 == gift_card와 wants의 불일치 --> gift_card를 하나씩 돌면서 dic의 key에 존재하는지를 판단
# 존재하는 경우에는 동일하면 갯수와 result(디폴트는 want의 길이)를 하나씩 빼자
# 결국 gift_card에 존재하는 것을 다 빼고 남는 것이 원치않는 상품의 갯수가 될 것이다.

def git_card(gift_cards, wants):
    dic = {}
    result = len(wants)
    for thing in wants:
        if thing not in dic:
            dic[thing] = 1
        else :
            dic[thing]= dic[thing] +1
    for key in gift_cards:
        if key in dic.keys() and dic[key] > 0:
            dic[key] -= 1
            result -=1
        else:
            continue
    return result

git_cards = [4,5,3,2,1]
wants = [2,4,4,5,1]

print(git_card(git_cards,wants))
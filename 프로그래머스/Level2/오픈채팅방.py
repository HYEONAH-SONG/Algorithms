# 나간 후, 새로운 닉네임으로 다시 들어간다.
# 안나가고, 채팅방에서 닉네임을 변경한다.

# 딕셔너리 활용 문제
def solution(record):
    answer = []
    name = dict() # key : uesr ID / value : nickname
    for message in record:
        if (message.split(' ')[0] == 'Enter') | (message.split(' ')[0] == 'Change'):
            name[message.split(' ')[1]] = message.split(' ')[2]

    for message in record:
        if message.split(' ')[0] == 'Enter':
            answer.append(name[message.split(' ')[1]]+"님이 들어왔습니다.")
        elif message.split(' ')[0] == 'Leave':
            answer.append(name[message.split(' ')[1]]+"님이 나갔습니다.")
        else: # change는 출력하지 않는다.
            continue
    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))
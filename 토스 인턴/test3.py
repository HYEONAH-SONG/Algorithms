# 조직 ID,조직명,상위 조직 ID,소속 팀원 수
# 1,토스팀,,1
# 2,인터널 트라이브,1,1
# 3,인터널 매니저 팀,2,7
# 4,비바 플랫폼 팀,2,14
# 5,아웃터널 트라이브,1,2
# 6,가이드 팀,5,4
# 7,피트아웃 사일로,5,11
# 인접 array를 사용

def solution(csv_string, keyword):
    number = 0 # 총 팀원의 수
    inform = []

    string = csv_string.split('\n')[1:]
    for i in string:
        inform.append(i.split(','))
    print(inform)
    member = [0 for i in range(len(inform))]
    for j in inform:
        if j[0] == '1':
            member[0]= [j[1],int(j[3])]
        else:
            member.insert(int(j[2]),[j[1],int(j[3])])
    print(member)
    for k in inform:
        if keyword in k[1]: # 검색어를 찾은 경우
            number += int(k[3]) # 해당 원소의 멤버 수 더하기

    return -1

csv_string = "조직 ID,조직명,상위 조직 ID,소속 팀원 수\n1,토스팀,,1\n2,인터널 트라이브,1,1\n3,인터널 매니저 팀,2,7\n4,비바 플랫폼 팀,2,14\n5,아웃터널 트라이브,1,2\n6,가이드 팀,5,4\n7,피트아웃 사일로,5,11"
keyword = "아웃"
print(solution(csv_string, keyword))

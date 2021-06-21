# 이 리스트에서 중복해서 나타나는  'abc＇와 'opq＇를 제거한 리스트 new_s_list = ['abc', 'bcd', 'abba', 'cddc', 'opq’]를 생성하는 프로그램을 작성하시오. [10]
# Hint: 비어 있는 new_s_list를 생성한 후, s_list의 모든 원소를 하나하나 꺼내어 new_s_list에 삽입하도록 한다.
# 이 때 s_list의 원소가 new_s_list에 이미 포함되어 있지 않은 경우 new_s_list에 삽입하면 된다.

s_list = ['abc', 'bcd', 'abc', 'abba', 'cddc', 'opq', 'opq']
new_s_list = []
for i in s_list :
    if i in new_s_list:
        continue
    else :
        new_s_list.append(i)
print(new_s_list)
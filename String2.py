# 문장을 구성하는 단어를 역순으로 출력하는 프로그램을 작성하라
sentence = input()

s_list = sentence.split(' ')
s_list.reverse()
for i in s_list:
    print(i, end=' ')
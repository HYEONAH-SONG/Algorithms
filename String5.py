# 중복단어 없이 단어를 콤마로 구분해 사전순으로 출력하는 프로그램 작성
word = input()

word_list = word.split(' ')
word_list = set(word_list)
word_list = sorted(word_list)
# 리스트에서 문자열로 변환 join 사이에 ""를 넣음
print(','.join(word_list))
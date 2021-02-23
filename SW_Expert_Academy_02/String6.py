# 문자열을 입력하면 짝수 인덱스를 가진 문자들을 출력하는 프로그램 작성
word = list(input())
new_word = []
for i, alpha in enumerate(word) :
    if i % 2 ==0 :
        new_word.append(alpha)
print(''.join(new_word))
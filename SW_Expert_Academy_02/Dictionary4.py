# 리스트의 원소를 키로 하고 그 원소의 길이를 값으로 하는 딕셔너리 생성

fruit = ['   apple    ','banana','  melon']
dictionary = {}

#strip() : 공백 제거 함수
for key in fruit :
    dictionary[key.strip()] = len(key)
print(dictionary)
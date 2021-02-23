# 사용자가 입력한 문장에서 숫자와 문자를 구별해 각각의 개수를 출력하는 프로그램을 작성

anything = input()
dictionary = {"LETTERS":0, "DIGITS":0}

for k in anything :
    if 'a' <= k <= 'z' or 'A' <= k <= 'Z':
        dictionary["LETTERS"] +=1
    elif  '0' <= k <='9':
        dictionary["DIGITS"] += 1

print("LETTERS {}" .format(dictionary["LETTERS"]))
print("DIGITS {}" .format(dictionary["DIGITS"]))
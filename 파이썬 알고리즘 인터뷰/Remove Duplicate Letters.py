# 중복 문자 제거

str = "bcabcz"
str = sorted(set(str))
make = ""
for word in str:
    make+=word
print(make)

# 만약 핸재 문자가 스택에 쌓여 있ㅇ는 문자이고, 뒤에 다시 붙일 문자가 남아 있다면, 쌓아둔걸 없앤다.
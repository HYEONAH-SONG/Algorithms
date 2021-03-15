# 중복 문자 제거

str = "bcabcz"
str = sorted(set(str))
make = ""
for word in str:
    make+=word
print(make)
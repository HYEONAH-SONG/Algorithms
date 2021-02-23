
# 입력된 문자가 대문자일 경우 소문자 출력
# 소문자일 경우 대문자로 출력
# 알파벳이 아닐 경우엔 그냥 출력
# 출력 시 아스키코드 함께 출력

b = (input()) # 문자열
a = ord(b) # int

if a>=65 and a<=90 : # 대문자 아스키코드 65~90
    a1 = b.lower()
    print(b + "(ASCII: " + str(a) + ") => " + a1 + "(ASCII: " + str(ord(a1)) + ")")
elif a>=97 and a<=122 : # 소문자 아스키코드 97~122
    a2 = b.upper()
    print(b + "(ASCII: " + str(a) + ") => " + a2 + "(ASCII: " + str(ord(a2)) + ")")
else:
    print("(ASCII: "+ str(a) + ")")

# 회문 여부를 판단하는 코드를 작성

s= input()

print(''.join(reversed(s)))
if s == s[::-1] :
    print("입력하신 단어는 회문(Palindrome)입니다.")
else :
    print("입력하신 단어는 회문(Palindrome) 아닙니다.")
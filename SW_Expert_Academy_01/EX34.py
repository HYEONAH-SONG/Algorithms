#반목문을 이용해 단어의 순서를 거꾸로 해 반환하는 함수를 작성하고
#그 함수를 이용해 회문(앞뒤 어느 쪽에서도 같은 단어, 말) 여부를 판단하는 코드를 작성

def palindrome(str) :
    str_2 = str[::-1]
    print(str_2)
    if str == str_2 :
        print("입력하신 단어는 회문(Palindrome)입니다.")
    else :
        print("입력하신 단어는 회문(Palindrome)이 아닙니다.")


str_ = input()
palindrome(str_)
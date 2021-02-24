# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램

import sys
sys.stdin = open("input.txt")

word = (input()).upper()


dict1 = dict() # 가장 많이 사용된 알파벳 알아내기 위한 딕셔너리
for i in word :
   if i in dict1 :
        dict1[i] +=1
   else:
        dict1[i] =1

m = max(dict1.values())
cnt =0
for key, i in dict1.items():
    if i == m :
        cnt += 1
        j = key
if cnt > 1:
    print("?")
else :
    print(j)


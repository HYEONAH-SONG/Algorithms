import sys
sys.stdin = open("input.txt")

num = int(input()) # 단어의 개수
cnt = 0 # 그룹 단어 갯수

for _ in range(num):
    word = input()
    for i in range(len(word)):
        if ((word[i] in word[i+1:]) and (word[i]!=word[i+1])) :
            break
    else:
        cnt = cnt +1
print(cnt)
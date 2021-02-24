import sys
sys.stdin = open("input.txt")

'''
그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 
예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다. 
단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.
'''

num = int(input()) # 단어의 개수
cnt = 0 # 그룹 단어 갯수

for _ in range(num):
    word = input()
    for i in range(len(word)):
        if ((word[i] in word[i+1:]) and (word[i]!= word[i+1])) :
            break
    else:   # if문에 해당안되면 계속 for문을 돌다가 for문의 마지막까지 가면 실행하는 문장 --> for else 문
        cnt = cnt +1
print(cnt)
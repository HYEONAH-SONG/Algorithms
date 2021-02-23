# 10진수를 2진수로 변환하는 프로그램

num = int(input())
binary = (1,1)
mod = []
while binary[0] >= 1 :
    binary = divmod(num,2)
    num = binary[0]
    mod.insert(0,binary[1])
    print(mod[0], end="")



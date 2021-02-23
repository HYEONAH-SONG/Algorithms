# while문을 이용해 아래와 같이 별(*)을 표시하는 프로그램을 만드십시오.

star = 7
space = 0
while star > 0 :
    print(" "* space+"*"*star+" "* space)
    space +=1
    star-=2


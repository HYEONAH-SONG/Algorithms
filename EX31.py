'''
for문을 이용해 아래와 같이 별(*)을 표시하는 프로그램을 만드십시오.
    *
   **
  ***
 ****
*****
'''


star = 1
blank = 4

for num in range(5) :
     print(" "*blank + "*"* star)
     star +=1
     blank -=1
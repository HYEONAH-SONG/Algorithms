# 어떤 한 양의 정수를 입력하여 그 숫자에 0~9가 몇 번 사용되었는지 표시하십시오.
# count 문제는 dictionary를 사용하는 것이 좋다

num = input()

data = {'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}

for type in num :
    data[type] += 1
print (0,1,2,3,4,5,6,7,8,9)
print(data["0"],data["1"],data["2"],data["3"],data["4"],data["5"],data["6"],data["7"],data["8"],data["9"])

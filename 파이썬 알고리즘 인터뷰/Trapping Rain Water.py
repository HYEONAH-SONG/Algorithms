# 높이를 입력받아 비 온 후 얼마나 많은 물이 쌓일 수 있는지 계산하라

height = [0,1,0,2,1,0,1,3,2,1,2,1]
# 0 ~ 11 인덱스 존재

def findRain(heght_list):
    stack = [] # 높이의 변화 체크
    water =0  # 쌓일 수 있는 물
    for i in range(len(heght_list)-1):
        if stack and heght_list[i] > stack[-1] :
            top = stack.pop()
            stack.append(heght_list[i])
        elif not stack :
            stack.append(heght_list[i])
        elif stack and heght_list[i] < stack[-1] :
            water += min(stack[-1]-heght_list[i],heght_list[i])
        else :
            continue
        print(i,water)

findRain(height)

def findRain2(heght_list):
    stack=[]
    for i in range(len(heght_list)):
        while heght_list[i]:
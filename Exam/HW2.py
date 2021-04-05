# 일차 방정식 구하기
# 2점의 좌표를 입력받아서 이 점들을 통과하는 직선 방적식을 구하시오
# 직선의 기울기를 게산할 때, 항상 분모가 0인지를 검사해야 한다.

first_x = int(input('첫 번째 점의 x좌표:'))
first_y = int(input('첫 번째 점의 y좌표:'))
second_x = int(input('두 번째 점의 x좌표:'))
second_y = int(input('두 번째 점의 y좌표:'))

def linear_equation(first_x,first_y,second_x,second_y):
    linear =''
    inclination = 0
    if first_x != second_x:
        inclination = float(second_y-first_y)/(second_x-first_x)
        linear = str(inclination) + 'x + ' + str(inclination*(-first_x) + first_y)
    else:
        linear = 'x='+ str(first_x)
    return linear

print(linear_equation(first_x,first_y,second_x,second_y))
#print(linear_equation(first_x,first_y,second_x,sec ond_y))
#rv = stats.norm(mu,sigma)
#rv = stats.norm(mu,sigma)
#rv = stats.norm(mu,sigma)
#rv = stats.norm(mu,sigma)
#rv = stats.norm(mu,sigma)
#rv = stats.norm(mu,sigma)
#rv = stats.norm(mu,sigma)
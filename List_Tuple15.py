str = input() # 콤마(,)로 구분된 정수 값을 입력
list_=[]

new =str.split(',')
for key in new:
    key = int(key)
    list_.append(key)

print(list_)
print(tuple(list_))
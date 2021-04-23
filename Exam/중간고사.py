
n = int(input())

x=0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            x =x+1
            print("i: {} j:{} k:{},x : {}".format(i,j,k,x))
print(x)
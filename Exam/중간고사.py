
n = int(input())

x=0
for i in range(n):
    for j in range(n+1):
        for k in range(j+1,n):
            x =x+1
print(x)
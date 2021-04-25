n= 20 #10100
s =""
v =1
while v<=n//2:
    v*=2
while v>0:
    if n<v:
        s+="0"
        #print("n<v",n,v)
    else:
        print("n>=v",n,v)
        s+="1"
        n=n-v
    v=v//2
print("s:",s)
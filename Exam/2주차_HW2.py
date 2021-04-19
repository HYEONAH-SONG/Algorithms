# 1000만원을 은행에 저축하였다. 현재 이율은 5%이다. 몇 년이 지나야 원금의 2배가 되는가
money =  1000
rate = 0.05
year = 0

while money < 2000 :
    money= money*(1+rate)
    year +=1

print("투자 기간:",year)
print("총액:",money)

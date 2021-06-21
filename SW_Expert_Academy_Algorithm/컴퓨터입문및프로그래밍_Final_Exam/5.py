record = (100, 121, 120, 130, 140, 120, 122, 123, 190, 125)
print("일일 매출 기록:",record)
count = 0
before = record[0]
for i in record:
    if i < before :
        count +=1
    before = i
print("지난 10일동안 전일 대비 대출이 감소한 날은",count,"입니다.")
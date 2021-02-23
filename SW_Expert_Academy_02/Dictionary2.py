#아래의 상품 딕셔너리 데이터를 가격에 따라 내림차순으로 정렬하는 프로그램을 작성

product = {"TV": 2000000,"냉장고": 1500000,"책상": 350000,"노트북": 1200000,"가스레인지": 200000,"세탁기": 1000000}

sorted(product)
for key,value in product.items() :
   print("{}: {}".format(key,value)) #딕셔너리 key value 따로 출력 방법
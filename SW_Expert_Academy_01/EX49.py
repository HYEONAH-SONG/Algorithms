#list에 map 사용하기
#map은 리스트의 요소를 지정된 함수로 처리해주는 함수이다

list_pow = list(map(lambda x:x**2,range(1,11)))
print(list_pow)
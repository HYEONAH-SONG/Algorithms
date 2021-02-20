# 람다식 : lambda 인자 : 표현식
# fileter : 리스트에 들어있는 원소들을 함수에 적용시켜서 결과가 참인 값들로 새로운 리스트를 만들어준다

s_list = list (filter(lambda x: x%2 ==0, range(1, 11)))
print(s_list)
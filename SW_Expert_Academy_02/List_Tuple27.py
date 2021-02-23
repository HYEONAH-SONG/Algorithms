# 리스트 항목 중 중복이 되는 항목을 제거하는 함수를 정의
# set은 집합 자료형으로 중복을 허락하지 않는다
l =[12,24,35,24,88,120,155,88,120,155]

n_duplicate = sorted(set(l))
print(n_duplicate)
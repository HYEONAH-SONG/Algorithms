# 모든 곱의 합을 다 구하는 것이 옳을까? No --> A의 가장 작은 값과 B의 가장 큰 값을 순서대로 곱해서 더하는 것이 최솟값을 구하는 것
# 최솟값을 구하는 방법만 알면 순탄하게 풀 수 있는 문제
# 시간 복잡도 : O(NlogN)
def solution(A,B):
    m_sum = 0
    A.sort() # 오름차순 정렬
    B.sort(reverse=True) # 내림차순 정렬
    for i in range(len(A)):
        m_sum += A[i]*B[i]
    return m_sum
A, B =[1, 4, 2],[5, 4, 4]
print(solution(A,B))

# bfs : visited를 활용하기(2차원)
# 벽돌 뿌수기 1회 기능 제공
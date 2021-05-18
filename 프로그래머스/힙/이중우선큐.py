import heapq  # module import

def solution(operations):
    reverse_sign = lambda x: x * -1
    heap = []
    answer = []
    for i in operations:
        if i == "D 1": # 큐에서 최대값을 삭제한다.
            if heap:
                heap = list(map(reverse_sign,heap))
                heapq.heapify(heap)
                s = heapq.heappop(heap)
                heap = list(map(reverse_sign, heap))
                heapq.heapify(heap)
            else : continue
        elif i == "D -1": # 큐에서 최솟값을 삭제한다.
            if heap:
                heapq.heappop(heap) # 가장 작은 원소를 꺼내어 자동적으로 다름으로 작은 원소가 루트 노드가 됨
            else : continue
        else:
            heapq.heappush(heap, int(i[2:]))
            heapq.heapify(heap)

    if heap: # 큐가 비어있지 않은 경우
        answer.append(max(heap))
        answer.append(min(heap))
        return answer
    else:
        return [0,0]

operations = ["I 7","I 5","I -5","D 1"]
print(solution(operations))
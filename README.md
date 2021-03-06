# 파이썬 코딩 테스크 문법 총정리

1. #### 자주 출제되는 유형

   - 그리디 
   - 구현
   - DFS/BFS를 활용한 탐색

2. #### 요구사항에 따른 적합한 알고리즘 탐색

   - N 의 범위 500 : N^3
   - N 의 범위 2000 : N^2 
   - N 의 범위 100,000 : NlogN 
   - N 의 범위 10,000,000 : N

3. #### 대표적인 자료형 구분

   1. 리스트

      - ##### 리스트 컴프리헨션 

        **리스트의 초기화**하는 경우에 많이 사용된다

        ```python
        array = [i for i in range(10)]
        array = [i for i in range(10) if i%2 ==1 ]
        array = [i*i for i in range(10)]
        # 가장 많이 사용되는 때는 2차원 배열 초기화할 때
        array = [[0]*m for _ in range(n)]
        # m이 열이 되고 n이 행이 된다.
        ```

      - 리스트 관련 메소드

        - append/pop :  O(1)
        - sort()/sort(reverse=True) : O(NlogN)
        - 순서가 있기 때문에 인덱싱을 통해 값을 얻을 수 있음
       
      - 인덱스

        - 모든 인덱스는 왼쪽부터 시작한다 왼(0) ---> 오(size -1)
        - for a in list --> 리스트의 왼쪽 원소부터 차례대로 봄
   
2. 튜플
   
   - 튜플은 한 번 선언하면 변경이 불가능하다
      - 순서가 있기 때문에 인덱싱을 통해 값을 얻을 수 있음

   3. ##### 딕셔너리 ★★
   
      - Key 값을 이용해서 O(1)의 시간복잡도로 조회가능
   
      - 딕셔너리를 이용한 count
       찾고자 하는 키가 정의된 딕셔너리에 없는 경우에 사용
   
        > get(para1,paar2) : 찾고자하는 para1이 없는 경우에는 para2를 return 
   
        ```
            stages = [2, 1, 2, 6, 2, 4, 3, 3]
            stage_dict = {}
            stage_dict2 = {}
            people = len(stages) # 총 사람의 수
            for i in stages:
                stage_dict[i] = stage_dict.get(i,0) +1
        ```
   
        
   
   4. 집합(set)
   
      - 집합의 원소 값을 이용해서 O(1)의 시간복잡도로 조회가능
      - 중복을 허용하지 않는다
      - 순서가 없다
      
   5. 
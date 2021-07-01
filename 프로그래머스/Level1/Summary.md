# 그리디 알고리즘(Greedy Algorithms)

- #### 당장의 눈 앞에 보이는 최적의 상황만을 쫒는 알고리즘

- 기본적으로 무조건 큰 경우대로, 작은 경우대로, 무조건 긴 경우대로, 등으로 극단적으로 문제에 접근을 한다

  > 정렬(Sort) 기법이 함께 사용되는 경우가 많다.

- #### Example Code

  - [프로그래머스>체육복](https://github.com/HYEONAH-SONG/Algorithms/blob/master/Level1/%EC%B2%B4%EC%9C%A1%EB%B3%B5.py)

  ```
  def solution(n, lost, reserve):
      reserve_set = set(reserve).difference(set(lost))
      lost_set = set(lost).difference(set(reserve))
      # reserve에서 이전의 인덱스부터 확인해야한다
      for i in reserve_set:
          if i-1 in lost_set :
              lost_set.remove(i-1)
          elif i+1 in lost_set:
              lost_set.remove(i+1)
      answer = n - len(lost_set)
      return answer
  ```

  
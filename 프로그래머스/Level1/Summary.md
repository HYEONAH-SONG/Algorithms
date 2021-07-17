### 1.그리디 알고리즘(Greedy Algorithms)

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


> isdigit() : 문자열이 숫자로만 이뤄져있는지 판변하는 함수(하나라도 문자열이 있는 경우에 False를 리턴한다.)

### 2.소수 판별 코드

- 시간복잡도 O(N) : 비효율적

```
# 기본적인 소수 판별 방법(2부터 n-1까지 돌려보기)
def is_prime_number(x):
  # 2부터 (x - 1)까지의 모든 수를 확인
  for i in range(2, x):
  	# x가 해당 수로 나누어떨어지면
    if x % i == 0:
    	return False
  return True
  
print(is_prime_number(4)) # False
```
- 시간복잡도 O(N^(1/2)) : 개선되었지만 여러 수에 대한 소수 판별에서는 비효율적
  약수의 가운데 수를 기준으로 대칭적으로 곱을 통해 n을 만들수 있다는 것을 활용

```
import math

# 제곱근까지만 보고 소수를 판별하는 함수
def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x))+1):
    # x가 해당 수로 나누어 떨어진다면
    if x % i == 0:
        return False
    return True
```

- 시간복잡도 O(Nlog(logN)) : N이 1,000,000 이내로 주어지는 경우 활용할 것 => 이론상 400만번 정도 연산이고 메모리도 충분함
  1. 2부터 N까지의 모든 자연수를 나열한다.
  2. 남은 수 중에서 아직 처리하지 않은 가장 작은 수 i를 찾는다.
  3. 남은 수 중에서 i의 배수를 모두 제거한다.(i는 제거하지 않는다.)
  4. 더 이상 반복할 수 없을 때까지 2번과 3번의 과정을 반복한다. 

```python
import math

# 소수 판별 함수(에라토스테네스의 체)
def is_prime_number(n):
    # 2부터 n까지의 모든 수에 대하여 소수 판별
    array = [True for i in range(n+1)] # 처음엔 모든 수가 소수(True)인 것으로 초기화(0과 1은 제외)

    # 에라토스테네스의 체
    for i in range(2, int(math.sqrt(n)) + 1): #2부터 n의 제곱근까지의 모든 수를 확인하며
        if array[i] == True: # i가 소수인 경우(남은 수인 경우)
            # i를 제외한 i의 모든 배수를 지우기
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1

    return [ i for i in range(2, n+1) if array[i] ]

# N이 1,000,000 이내로 주어지는 경우 활용할 것 => 이론상 400만번 정도 연산이고 메모리도 충분함

print(is_prime_number(26))
```


# Algorithms

### Python 주요 문법

1. #### 자료형

```python
# 문자열 자료형에서는 ""와 '' 둘 중에 아무거나 써도 무방하다
print("나비")
print('나비')
# 나비
# 나비
```

2. #### 변수

```python
# 변수는 타입을 따로 선언하지 않아도 알아서 식별한다
name ="송현아"
age = 29
is_correct = age<20
#name은 string age는 int is_correct로 알아서 식별
```

3. #### 주석

```python
# #을 사용하면 한 줄 주석처리
'''
작은 따옴표 3개를 쓰면
여러 문장을 주석처리
'''
```

4. #### print 

```python
# +로 연결할 경우에는 모든 변수 타입이 string이 되어야 한다
# ,로 연결할 경우에는 string이 아니여도 되는데 ,를 기준으로 띄어쓰기가 적용된다
```

5. #### 슬라이싱

```
id_num = "990111-1234567"

print("성별 : "+ id_num[7]) # 7번째 자리
print("연 : "+ id_num[0:2]) # 0부터 1까지 = 0이상 2 미만
print("생년월일 : " + id_num[:6]) #0부터 5까지
```

6. #### 문자열처리함수

```
python ="Python is Amazing"
print(python.lower()) //소문자로 변환
print(python.upper()) //대문자로 변환
print(python.isupper()) //대문자인 경우 true 아닌 경우 false 반환
print(python[1].isupper()) //2번째 문자가 대문자인 경우 true 아닌 경우 false 반환
len(python) // 문자열 길이를 반환
python.replace("Python", "Java") //Python이 Java로 문자열 대체
index = python.index("n") //n의 인덱스 찾기 0부터 시작 주의 
index = python.index("n", index +1) //처음 n 말고 다음 n의 인덱스 찾기
python.count("n") //문자열에서 n이 몇 번 등장하는가
```



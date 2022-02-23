# 1. 2차원 리스트 복습

* List Comprehension을 통해 2차원 리스트 형태로 입력

* 예시 (8x8 체스판)

  ```python
  # 입력
  FFFFFFFF
  FFFFFFFF
  FFFFFFFF
  FFFFFFFF
  FFFFFFFF
  FFFFFFFF
  FFFFFFFF
  FFFFFFFF
  
  # List Comprehension
  chese = [list(input()) for _ in range(8)]
  print(chese)
  
  ```

* 흰 색 체스판에 올려져 있는 말의 개수는 어떻게 구할 수 있을까?

  * 흰 색 체스판 조건 : **짝수줄의 짝수 칸** or **홀수 줄의 홀수 칸**

    > **F**F**F**F**F**F**F**F ← 짝수 줄 (짝수 칸)
    > F**F**F**F**F**F**F**F** ← 홀수 줄 (홀수 칸)
    > **F**F**F**F**F**F**F**F
    > F**F**F**F**F**F**F**F**
    > **F**F**F**F**F**F**F**F
    > F**F**F**F**F**F**F**F**
    > **F**F**F**F**F**F**F**F
    > F**F**F**F**F**F**F**F**

  * 줄별로 하나하나씩 (가로로) 찾아보자!

  ```python
  board = [list(input()) for _ in range(8)]
  total = 0
  
  for i in range(8):
      for j in range(8):
          if i % 2 == j % 2 and board[i][j] == "F":
              total += 1
              
  print(total)
  ```

  * 세로로 보고 싶으면?
    * board의 인덱스를 board[j][i]로 바꾸면 됨!

  ```python
  board = [list(input()) for _ in range(8)]
  total = 0
  
  for i in range(8):
      for j in range(8):
          if i % 2 == j % 2 and board[j][i] == "F":
              total += 1
              
  print(total)
  ```

  * 3개씩 끊어서 회오리 모양으로 탐색, 바깥에서 부터 달팽이 모양으로 탐색, ... 등은 어떻게 하면 될까?
    * 이것도 board의 인덱스 자리를 조작하면 됨!!!
    * 문제별로 다르니 하나하나 풀면서 발전시켜보기☆
  * 한 줄로도 작성할 수 있을까?
    * `print(sum(input()[i % 2 :: 2]).count("F") for i in range(8))`
    * input()은 "F" 8개로 이루어진 한 줄, 



# 2. 딕셔너리 (Dictionary)

## 1) 해시 테이블 (Hash Table)

### (1) 딕셔너리

* 파이썬에는 기본적으로 **딕셔너리(dict) 자료구조**가 내장되어 있음!

  * **<u>non-sequence & Key:Value</u>**

  ```python
  {
  "name":"kyle",
  "gender":"male",
  "address":"Seoul"
  }
  ```

  * <u>Key는 immutable 해야함</u> (리스트 등 mutable 자료구조는 못들어감)



### (2) 해시 테이블

>  **<u>Key:Value가 저장되는 원리는?</u>**

1. 일단 **리스트**를 이용해 Key:Value를 저장해보자.

   * 2차원 리스트 처럼, 0번째 index에는 Key를, 1번째 index에는 Value를 저장하는 것!

   * Key값을 이용해 Value를 조회하려고 하면? 하나하나씩 다 검사해야됨! : **<u>O(n)</u>**

2. 딕셔너리는 **해시 테이블(Hash Table)**을 이용하여 Key:Value를 저장함!

   * 해시 테이블은 마치 사람처럼 한 번에 찾을 수 있음! (<u>*딕셔너리는 빠르다!*</u>)

   * Key값은 각각 해시 테이블의 Index와 연결, Value값을 한 번에 찾음! : **<u>O(1)</u>**



### (3) 해시 함수

> <u>그렇다면 **Key 값과 해시 테이블의 Index를 연결해주는 규칙은?**</u>

* **해시 함수**가 정해줌! (해시 함수는 누가 만들었는지에 따라 다름, 파이썬의 딕셔너리를 만든 개발자가 이미 해시 함수 규칙을 만들어놓음!)
  * ex) `Key % 10`
* 해시 테이블의 시간 복잡도는 Key값이 해시 함수를 지나가는 시간! : **O(1)로 고정됨!**
* Git commit 했을 때, 나오는 ID도 해시 값이라고 함! ex) `2C94EF1P`
* 이런 특징을 이용해서, 웹사이트의 아이디 및 비밀번호도 저장됨!
  * 아이디 == Key, 비밀번호는 해시 함수를 지나가서 해시테이블에 저장되는 Value!



## 2) 딕셔너리 

### (1) 딕셔너리 기본 사용법

> dict도 <u>연산</u>(선언, 삽입, 수정, 삭제, 조회) <u>가능</u>한 자료구조!
>
> 해당 연산은 <u>해시 테이블을 사용</u>한다!

* 선언
  * `변수 = {key1:value1, key2:value2, ...}`
* 삽입/수정
  * `딕셔너리[key] = value`
  * 내부에 해당 key가 없으면 삽입, 있으면 수정
* 삭제
  * `del 딕셔너리[key]`
  * remove는 리스트에만 쓸 수 있지만, del은 리스트와 딕셔너리 요소 삭제에 모두 사용가능!
* 조회
  * `딕셔너리[key]`
    * 내부에 해당 key가 없으면 <u>error</u> 발생!
  * `딕셔너리.get(key)` : ★★★★★
    * <u>내부에 해당 key가 없으면 `None`이라는 반환 값이 나옴!</u>
    * `if 딕셔너리.get(key) == None` 이렇게 사용할 수 있음!
    * `딕셔너리.get(key, "없음")` : 없을 때 반환 값을 지정할 수도 있음!!!



## 3) 딕셔너리 메서드

### (1) .keys()

* 딕셔너리의 key 목록을 반환한다.

  ```python
  a = {
      "name":"kyle",
      "gender":"male",
      "address":"Seoul"
  }
  
  print(a.keys())    #dict_keys(['name', 'gender', 'address'])
  
  for key in a.keys():
      print(key)     #name, gender, address가 한 줄에 하나씩 출력
  
  for key in a:
      print(key)     #기본적으로 in dict를 쓰면 dict의 key를 반환한다! (위와 동일 결과)
  ```

  * in 연산자 비교 (list, set, dict)

  ```python
  a = 3
  b = [1,2,3,4,5]
  c = {1,2,3,4,5}
  d = {1:1, 2:2, 3:3, 4:4, 5:5}
  
  if a in b    #list는 하나하나 확인하기 때문에 오래걸림 : O(n)
  if a in c    #set도 사실 해시 테이블로 구성되어있음 : O(1)
  if a in d    #모두 True로 나오지만 set, dict가 list보다 훨씬 빠름!
  ```

  * 리스트 원소개수가 많을 때 in 연산자를 쓰려면, `in set(list)`를 활용하자...!



### (2) .values()

* 딕셔너리의 value 목록을 반환한다.



### (3) .items()

* 딕셔너리의 key, value 쌍을 반환한다.

  ```python
  for key, value in a.items():     #보통 .items() 사용시 다중할당을 활용!
      print(key, value)
  ```





# 3. 코딩테스트 꿀팁

* 다른 언어에서는 사용하지 못하는, Python만이 할 수 있는 코드 ([URL](https://github.com/VSFe/Algorithm_Study/blob/main/Concept/New/00_Special/Pythonic_Code_For_Coding_Test.md#pythonic-code-for-coding-test))


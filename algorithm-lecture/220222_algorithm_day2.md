# 1. 알고리즘의 시간 복잡도

## 1) 자료 vs 자료구조

* `자료 == Data`

  * int, float 같은 것을 <u>자료형</u>이라고 하고, **데이터를 메모리(RAM)에 저장**한다.
  * ex) 3 - 연산 불가(메소드 없음!)

* `자료 구조 == Data Structure`

  * 데이터를 읽기, 쓰기, 삽입, 삭제, 탐색할 수 있는 **연산 기능을 제공**한다.
  * ex) [3, 4, 5] - <u>append, pop, remove, insert 등 메소드로 연산가능!</u>
  * 다수의 데이터를 효율적으로 저장하고 조작할 수 있으므로, **<u>자료 구조가 알고리즘 구현의 기본 재료가 된다!</u>**

  > 즉, **자료구조의 특성**을 알아야 알고리즘을 구현할 수 있다!




## 2) 알고리즘 소요시간

### (1) 알고리즘 성능 평가기준

* 좋은 알고리즘이란 무엇일까요?

  * 효율성이 좋은 알고리즘
  * 성능이 좋은 알고리즘

  > 시간 복잡도의 측면에서, Input을 넣은 후 **Output이 나오는 시간이 <u>짧게 걸리는</u> 알고리즘!**



### (2) 알고리즘 소요시간 측정방법

* 그렇다면 알고리즘 소요 시간은 어떻게 측정할까요?

1. **타이머로 재기**
   * 컴퓨터 사양, 하드웨어 성능에 따라 같은 알고리즘이라도 측정시간이 달라짐. 환경에 영향을 받지 않는 <u>객관적 기준</u>이 필요!

2. **기본연산 횟수**

   * `기본연산`이란 단위시간 1이 소요되는 기본적인 연산. 즉, 단위 연산
     * ex) 할당, 산술, 비교, 반환 ...

    * 즉, `기본연산의 총 횟수 == 알고리즘의 소요 시간`


   * 예시 코드에서 기본연산 횟수를 세어보자

      ```python
        def count(word, char):    #input
            total = 0
            for i in word:
                if i == char:
                    total += 1
            return total          #output
      
      count("apple", "p")
      ```

      * `total = 0`은 연산 1개 (할당)
      * `for i in word` 는 연산 5개 (i가 할당될 때마다 1개)
      * `i == char` 는 연산 5개 (5개 i를 각각 char와 비교)
      * `total += 1` 은 연산 4개 (덧셈, 할당이 2번 일어남)
      * 총 15번의 연산이 일어남. 즉, 알고리즘 소요시간 == 15

   * 하지만, <u>입력에 따라 알고리즘별 소요시간 크기우위가 달라질 수도 있음!</u> (어떨 때는 A알고리즘이 빠르고, 다른 때는 B알고리즘이 빠르게 나오고...)

3. **최악의 입력**

   * 가장 기본연산이 많이 일어나는 <u>최악의 입력 n개</u>가 들어온다고 가정하고 측정한다.

   * 즉, 위의 total += 1 연산이 매번 실행되는 경우

    ```python
    count("aaaaa","a")
    ```



## 3) 시간 복잡도와 Big-O 표기법

### (1) **시간 복잡도(Time Complexity)란 ?**

* 단순하게 <u>알고리즘의 수행 시간</u>을 의미
  
  > 시간 복잡도가 높으면 느린 알고리즘!
  >
  > 시간 복잡도가 낮으면 빠른 알고리즘!



* 시간복잡도에 따라 <u>알고리즘의 성능을 비교</u>해보자

  * Input이 `n`개일 때 작성자별 시간 복잡도를 수식으로 나타내면?

    * A 작성자 : 6n + 4 (시간 복잡도가 <u>선형으로 증가</u>)

    * B 작성자 : 3n + 2 (<u>선형 증가</u>)
    * C 작성자 : 3n^2 + 6n + 1 (<u>제곱으로 증가</u>)
    * Input이 `1`개 일 때) A : 10, B : 5, C : 10
    * Input이 `5`개 일 때) A : 34, B : 17, C : 94

  * **n이 무한대라면?** A, B작성자는 비교의 의미가 없다. C 작성자는 의미가 있다.



### (2) Big-O 표기법이란?

* 입력 n이 무한대로 커진다고 가정하고 시간 <u>복잡도를 간단하게 표시</u> 하는 것

  * 수 많은 알고리즘이 있기 때문에 최대한 간단히 표시하자! (약속)

* **<u>최고차항</u>만 남기고 계수와 상수를 제거**

  * A 작성자 : O(n)

  * B 작성자 : O(n)

  * C 작성자 : O(n^2)

* <u>다양한 시간 복잡도 종류 살펴보기</u>

  * O(2^n)

  * O(n^2)

  * O(n log n)

  * O(n) : 입력이 변함에 따라 n에 비례하여 시간복잡도가 변함

  * O(log n) : log n은 log2가 생략되어있다고 생각하면 편함 

  * O(1) : 입력이 변해도 입력 1개만 시간복잡도 검사

    > O(n) 과 O(log n)의 차이?
    >
    > => log n은 업다운 게임이라고 생각하면 됨! 이진분류 알고리즘에 사용됨!

* <u>실제 문제에서</u> 어떻게 적용?

  * 실제 문제는 "초" 단위로 제한 시간이 주어지고, 시간복잡도도 정확히 예측하기 어렵다.

  * 어림짐작 해서, **보통 컴퓨터는 1초에 1억 번 연산으로 계산 (국룰)**

  * 즉, 시간제한이 1초일 때 n개 입력을 넣으면 알고리즘 전체 연산이 1억번 이하로 나와야 함!

  * 아래와 같은 문제를 풀어보자.

    ```markdown
    문제 : 연속된 숫자들의 합 구하기
    제한 시간 : 1초
    입력 : 자연수 N이 입력된다. (1 <= N <= 1,000,000,000)
    출력 : 
    ```

    ```python
    ## 첫 번째 방법 - 일일히 더하기
    
    def get_total(n):
    	total = 0
        for i in range(1, n+1):
            total += i
        return total
    
    print(get_total(10))     #O(n), 10을 넣으면 10번 계산, 10억번 넣으면 10억번 계산(계산이 엄청 오래 걸림)
    ```

    ```python
    ## O(1)로 풀 수 있을까?
    
    def get_total(n):
    	return (n + (n+1)) // 2
    
    print(get_total(1000000000))    #O(1)이기 때문에 넣으면 바로 나옴!
    ```

  * 입력 n개로 for문 1번 돌아가면 O(n), O(n^2)은 이중 for문이라고 생각하면 됨.

  * **같은 동작을 하는 알고리즘이라 하더라도 시간 복잡도에 따른 성능이 달라지고, 곧 시험에서 취업 여부가 달라진다!**

  * 내장 함수, 메서드의 시간복잡도가 모두 달라 확인할 필요가 있다!

    ![Big O Cheat sheet](220222_algorithm_day2.assets/image-20220222125947753.png)

  * 즉, for문 1번이라고 무조건 O(n)인것이 아니다. <u>for문 안에 O(n)의 내장 함수(replace 등)를 사용했다면, 이중 for문과 다를게 없기 때문!!!</u>



# 2. 리스트 (List)

## 1) 배열 (Array)

* ***여러 데이터들이 연속된 메모리 공간에 저장되어있는 자료구조** (가장 원시적인 자료구조) : **O(1)***

* 인덱스(Index)를 통해 데이터 빠르게 접근 가능

* 배열의 <u>길이는 변경 불가능</u>, <u>데이터 타입 고정됨</u>

* C, Java에 배열이라는 개념이 있음!

  * C 언어 배열 할당 예시

    ```c
    int arr[5] = {70, 80, 20, 100, 90};
    
    # int 데이터 타입
    # [5] 길이
    # 바꾸고 싶다면 새로 만들어야 함!
    ```



## 2) 연결 리스트 (Linked List)

* ***데이터가 담긴 여러 노드들이 순차적으로 연결된 형태의 자료구조** : **O(n)***
* 데이터에 접근하려면 맨 처음 노드부터 순차적으로 탐색
* 연결 리스트의 <u>길이는 자유롭게 변경가능</u>(삽입, 삭제가 편리), <u>다양한 데이터 타입 저장가능</u>
* 데이터가 메모리에 연속적으로 저장되지 않음



## 3) 파이썬의 리스트 (List)

* ***배열(Array)과 연결 리스트(Linked List)의 특징을 모두 가지고 있는 것이 파이썬의 리스트(List)***
* <u>인덱스로 접근가능, 길이 자유롭게 변경가능, 다양한 데이터 타입 저장가능</u>
* 파이썬 리스트의 삽입, 삭제 메서드
  * .append(원소)
    * 리스트 맨 끝에 새로운 원소 추가 : **O(1)**
  * .pop(인덱스)
    * 특정 인덱스의 값을 <u>삭제하면서 동시에 반환</u> (.remove()는 지우기만 함!)
    * .pop() - 맨 끝 원소 삭제 및 반환 : **O(1)**
    * .pop(i) - i로 지정된 인덱스 삭제, 반환 후 자리 앞으로 당기기 : **O(n)**



# 3. 리스트 활용 알고리즘

## 1) 리스트 관련 내장 함수

* len(), sum(), max(), min(), sorted(), reversed(), zip() - 다른 자료형에도 모두 사용 가능



* len()
  * 리스트의 **길이**(원소의 개수)를 반환 : O(1) - 찾아보기

* sum()
  * 입력 받은 리스트의 모든 원소의 **합**을 반환 : O(n)

* max()
  * 입력 받은 리스트의 원소 중 **최댓값**을 반환 : O(n)

* min()
  * 입력 받은 리스트의 원소 중 **최솟값**을 반환 : O(n)

* sorted()

  * 입력 받은 리스트를 **정렬**한 후 리스트로 반환 (사전순, 오름차순) : O()

  * 새로운 리스트가 생기는 것이므로 기존 값은 변화 없음

  * `reverse=True` 옵션은 거꾸로

* reversed()

  * 입력 받은 리스트의 순서를 **거꾸로** 바꿔서 반환 : O()

  * **a[::-1]**과 비슷한 기능을 함

  * 단, 반환 값이 리스트가 아니므로 타입 변환이 필요
    * `list_reverseiterator at ~~~~` 이렇게 나와서 `list()`로 감싸줘야함



> 궁금한 것은 'Timsort' 검색해서 찾아보기!



## 2) List Comprehension

* `List Comprehension` (리스트 컴프리헨션, 리스트 내포)

  * 리스트를 **코드 한 줄만 작성**하여 만들 수 있는 유용한 도구

  * 짧을 뿐만 아니라 <u>효율도 좋고, 실무에서 많이 씀!</u> (굉장히 권장)

    ```python
    ## for문으로 list 생성
    numbers = []
    for i in range(5):
        numbers.append(i)
        
    print(numbers)
    
    ## List Comprehension
    numbers = [i for in range(5)]
    print(numbers)
    
    ## if문 필터링도 가능
    numbers = []
    for i in range(5):
        if i % 2 == 1:           # 0부터 9까지 홀수만 출력
        	numbers.append(i)
        
    print(numbers)
    
    ## List Comprehension
    odd_numbers = [i for i in range(10) if i % 2 == 1]
    print(odd_numbers)
    ```

    

## 3) 2차원 리스트

* 2차원 리스트 형태로 입력받고 조작하는 방식의 문제가 자주 나옴
  * ex) DFS, BFS
* List Comprehension을 사용하면 간편하게 입력 받을 수 있음!



# 4. PEP8

[한국어 번역](https://zerosheepmoo.github.io/pep8-in-korean/doc/introduction.html)

* <u>파이썬의 코드 스타일 규칙</u>!
* 전세계적으로 사용자간 코드 스타일을 일치시켜 원활한 코드공유를 가능하게 함!
* Vscode에서는 extension을 다운받으면 단축키 `Shift + Alt + F` 로 autopep8 기능 사용가능!

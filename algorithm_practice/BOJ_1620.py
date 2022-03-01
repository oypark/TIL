## 나는야 포켓몬 마스터 이다솜

n, m = map(int, input().split())

pocketmon = {}
for i in range(1,n+1):
    name = input()
    pocketmon[i] = name
    pocketmon[name] = i


for j in range(m):
    question = input()
    if question.isnumeric():
        print(pocketmon[int(question)])
    else:
        print(pocketmon[question])


## 해당 문제는 PyPy3으로 넣어야 시간초과가 나지 않음!
## PyPy3은 Python3의 실행시 시간이 매우 오래 걸리는 단점을 개선하고자 JIT컴파일 방식을 도입한 것

## 즉, 프로그램 실행 전 컴파일 하는 인터프리터 언어(Pyhotn)와는 다르게 프로그램을 실행하는 시점에서 필요한 부분들을 즉석으로 컴파일 한다.
## 인터프리트 하면서 자수 쓰이는 코드를 캐싱하는 기능이 있고, 메모리를 조금 더 사용하여 그것들을 저장하고 실행속도를 개선할 수 있다.

## 따라서 간단한 코드는 Python3가 메모리, 속도 측면에서 우세하지만 반복적인 동작이 많은 복잡한 코드에서는 PyPy3가 우세하기 때문에 코드 상황에 맞추어 두 구현체를 적절하게 사용하는 것이 효율적이다.


## 다른 풀이

n, m = map(int, input().split())

numbers = {}
names = {}

for i in range(1, n+1):
    name = input()
    names[i] = name
    numbers[name] = i

for _ in range(m):
    question = input()
    # .isdecimal()은 값이 int형으로 변환 가능한 형식인지 확인(제곱, 분수, 거듭제곱 등은 제외)
    if question.isdecimal():
        print(names[int(question)])
    else:
        print(numbers[question])


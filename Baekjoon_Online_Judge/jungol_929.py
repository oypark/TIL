## 기존 풀이
n = int(input())
list = ["No."+str(i+1) for i in range(n)]
print(list)

## 피드백
# 1. f-string 이용해서도 고려해보기
# 2. list 변수명 바꾸기

## 새로운 풀이
n = int(input())
numbers = [f"No.{i+1}" for i in range(n)]
print(numbers)
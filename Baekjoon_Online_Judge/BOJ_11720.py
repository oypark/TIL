## 최초풀이
# n = int(input())
# number = input()
# list = []

# for i in range(n):
#     list.append(int(number[i]))

# print(sum(list))


## 피드백
# 1. list는 파이썬 내장함 수 이름이므로 다른 이름으로 바꿔보기
# 2. 애초에 input을 받을 때 map을 통해서 받아보기

n = int(input())
numbers = list(map(int, input()))
print(sum(numbers))
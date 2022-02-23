## 기존 풀이

# n = int(input())
# number = []

# for i in range(n):
#     num = int(input())
#     number.append(num)

# for i in range(n):
#     print(sorted(number)[i])


## 피드백
# 정답은 맞지만, 효율성 측면에서 고려해보기.
# for문이 1번 반복될 때마다 sorted를 통해서 정렬하고 있음.
# 정렬은 딱 한 번만 하면 됨!


## 새로운 풀이 - 시간 훨씬 단축됨!

n = int(input())
numbers = sorted([int(input()) for _ in range(n)])

for number in numbers:
    print(number)
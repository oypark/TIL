## 2차원 리스트 이해

## input은 다음과 같은 형태로 입력
# 3 4
# 1 2 3 4
# 5 6 7 8
# 9 0 1 2


n, m = map(int, input().split())      # n은 행, 4는 열 갯수


# for문 활용
# numbers = []
# for i_ in range(n):
#     number = list(map(int, input().split()))
#     numbers.append(number)

# list comprehension 활용
numbers = [list(map(int, input().split())) for _ in range(n)]


print(numbers)    #output, [[1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 1, 2]]


## 2차원 list 활용, 원소 하나씩 접근해서 출력해보기
for i in range(n):
    for j in range(m):
        print(numbers[i][j], end=" ")     # 4개는 띄어쓰기로 출력
    print()                               # 다음 줄로 바꾸고 또 4개씩 출력



## 2차원 list 초기화 시 주의사항
list_c = [[0]*4 for _ in range(2)]
list_d = [[0]*4] * 2     #흔히 하는 실수!

list_c[0][0] = 1
print(list_c)    #list_c는 곱셈으로 [[0]*4]를 복사했기 때문에, 얕은 복사가 적용됨. 열 인덱스가 1인 원소가 모두 바뀜.

list_d[0][0] = 1
print(list_d)    #list_d는 list comprehension으로 복사했기 때문에, 원하는 대로 잘 적용됨.
## 입력 예시
# 3 6 9
# 8 5 2
# 9 8 7
# 6 5 4

first_a = [list(map(int, input().split())) for _ in range(2)]
second_a = [list(map(int, input().split())) for _ in range(2)]

for i in range(2):
    for j in range(3):
        print(first_a[i][j]*second_a[i][j], end=" ")
    print()
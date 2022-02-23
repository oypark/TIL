first_array = [list(map(int, input().split())) for _ in range(2)]
second_array = [list(map(int, input().split())) for _ in range(2)]      # Alt + Shift + ↓ : 한 줄 복사


## for문 활용
for i in range(2):
    for j in range(4):
        print(first_array[i][j]*second_array[i][j], end=" ")
    print()


## list comprehension - list 안에 넣고 또 이중 for문 돌려서 출력해야하기 때문에 위처럼 이중 for문안에서 바로 프린트 하기!!
# multiple_array = [[first_array[i][j]*second_array[i][j] for j in range(4)] for i in range(2)]
# print(multiple_array[0], multiple_array[1], sep="\n")
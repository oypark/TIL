list_a = [list(map(int, input().split())) for i in range(2)]
list_b = [list(map(int, input().split())) for i in range(2)]

for i in range(2):
    for j in range(4):
        print(list_a[i][j]*list_b[i][j], end=" ")     # i == 0일 때 모든 칸 보고 / i == 1일 때 모든 칸 보고
    print()                                          # 한 줄 띄우기 / 한 줄 띄우기
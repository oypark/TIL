## 직사각형 네개의 합집합의 면적 구하기

square_set = set()
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            square_set.add((x,y))

print(len(square_set))


## 다른 풀이

board = [[0] * 100 for _ in range(100)]

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            board[i][j] = 1

print(sum(sum(line) for line in board))

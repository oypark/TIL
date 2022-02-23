# 하얀 칸

chess_board = [list(input()) for _ in range(8)]
# print(chess_board[0][0])    #왜 .이 안나올까... => input이 붙어있었는데 split()써서 문자열 전체로 인식됨...!

count = 0
for i in range(8):
    for j in range(8):
        if (i+j) % 2 == 0 and chess_board[i][j] == 'F':
            count += 1

print(count)

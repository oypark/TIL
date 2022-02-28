## 스도쿠 채점

def is_correct(sudoku):
    for line in sudoku:
        if len(set(line)) < 9:     #1~9 중 하나라도 없으면!(중복이 있다는 말!)
            return False
    return True


for n in range(1, int(input()) + 1):
    if n > 1:
        input()    # 스도쿠 사이 공백 입력

    sudoku = [list(map(int, input().split())) for _ in range(9)]

    sudoku3 = []
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            block = [sudoku[x][y] for x in range(i, i+3) for y in range(j, j+3)]
            sudoku3.append(block)
    
    if is_correct(sudoku) and is_correct(zip(*sudoku)) and is_correct(sudoku3):
        print(f"Case {n}: CORRECT")
    else:
        print(f"Case {n}: INCORRECT")
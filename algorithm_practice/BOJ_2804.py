def print_crossword(a, b):
    for i, char in enumerate(a):
        row_idx = b.find(char)
        if row_idx != -1:
            col_idx = i
            break

    for i, char in enumerate(b):
        if i != row_idx:
            print("." * (col_idx) + char + "." * (len(a) - col_idx-1))
        else:
            print(a)

a, b = input().split()

print_crossword(a, b)
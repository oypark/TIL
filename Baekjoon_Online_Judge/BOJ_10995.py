n = int(input())
line = "* " * n

## slicing 이용
for i in range(n):
    print(line)
    line = line[::-1]
    

## for문 이용
for i in range(n):
    # 짝수 번째 줄이면?
    if i % 2 == 0:
        print("* " * n)
    
    # 홀수 번째 줄이면?
    else:
        print(" *" * n)
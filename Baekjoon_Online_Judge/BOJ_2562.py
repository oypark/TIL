numbers = [int(input()) for _ in range(9)]    # for문에서 쓰지 않는 변수는 i대신 '_'로 표시하는 것이 관행
max_number = max(numbers)   # 변수를 또 사용할 때는 새로운 변수로 할당하는 것이 효과적
print(max_number)
print(numbers.index(max_number) + 1)
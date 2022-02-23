n = int(input())
numbers = []

for i in range(n):
    number = int(input())    #여기서 int 안씌워주면 문자열로 받아서 sorted에서 사전순으로 정렬됨 (2,17 넣었을 때 17이 먼저 나옴)
    numbers.append(number)

for number in sorted(numbers):
    print(number)
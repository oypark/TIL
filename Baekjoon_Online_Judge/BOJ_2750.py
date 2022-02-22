n = int(input())
number = []

for i in range(n):
    num = int(input())
    number.append(num)

for i in range(n):
    print(sorted(number)[i])
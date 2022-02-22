t = int(input())

for i in range(t):
    r, s = input().split()
    p = ""
    for j in s:
        p += j * int(r)
    print(p)

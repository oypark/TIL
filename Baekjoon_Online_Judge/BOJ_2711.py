## 오타맨 고창영
t = int(input())

for i in range(t):
    idx, str = input().split()
    str = str[:int(idx)-1] + str[int(idx):]
    print(str)
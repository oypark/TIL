## 듣보잡

n, m = map(int, input().split())

hear = set()
look = set()

for i in range(n):
    hear.add(input())

for j in range(m):
    look.add(input())

hearlook = sorted(list(hear.intersection(look)))
print(len(hearlook), *hearlook, sep="\n")

## 4080ms 시간이 너무 오래걸렸다... 조금 줄여보자!


n, m = map(int, input().split())
no_hear = {input(): 1 for _ in range(n)}
no_hear_see = []

for _ in range(m):
    no_see_person = input()
    if no_see_person in no_hear:
        no_hear_see.append(no_see_person)

print(len(no_hear_see), *sorted(no_hear_see), sep="\n")

## 3960ms 쬐끔 줄었다! ^,^
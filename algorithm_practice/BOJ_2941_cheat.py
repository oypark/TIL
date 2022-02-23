## replace 활용 (강사님 풀이)
word = input()
changes = ["c=","c-","dz=","d-","lj","nj","s=","z="]

for change in changes:
    word = word.replace(change, ".")

print(len(word))


## count 활용
word = input()
changes = ["=","-","dz=","lj","nj"]
total = len(word)

for change in changes:
    total -= word.count(change)

print(total)


## while문 활용 (다른 학생 답 cleasing)
word = input()
length = len(word)
i = 0
croatia = ["c=","c-","dz=","d-","lj","nj","s=","z="]
count = 0

while i < length:
    if i != length-1 and word[i:i+2] in croatia:
        i = i+2
    elif i < length-2 and word[i:i+3] in croatia:
        i = i+3
    else:
        i += 1
    count += 1

print(count)

## while문 활용 - 변형 (보조 강사님)
word = input()
answer = len(word)  # 일단 총 길이를 재고 여기서 차감하는 형태로 문제 구성

for idx, letter in enumerate(word):
    # 일단 길이 자체가 3이 이상인 경우만 첫번째 케이스를 해야함
    if letter == '=' and word[idx-1] == 'z' and idx >= 2 and word[idx-2] == 'd':  # dz=
        answer -= 2  # 3개짜리는 1개로 세야 하니까 -2 로 조정!
    elif letter == '=' and word[idx-1] in {'c', 's', 'z'}:  # set in 을 활용하는 경우 빠른 풀이 가능 O(1)
        answer -= 1  # c=, s=, z= 를 커버하는 케이스
    elif letter == 'j' and word[idx-1] in {'l', 'n'}:
        answer -= 1  # lj, nj 를 커버하는 케이스
    elif letter == '-' and word[idx-1] in {'c', 'd'}:
        answer -= 1  # c-, d- 를 커버하는 케이스

print(answer)
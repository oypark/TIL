## 명령 프롬프트 - cheat sheet

## 방법 1

n = int(input())
first, others = input(), [input() for _ in range(n - 1)]
pattern = ""

for i, char in enumerate(first):
    for other in others:
        if char != other[i]:
            pattern += "?"
            break    # for문을 break
        else:
            pattern += char

print(pattern)


## 방법 2 - 훨씬 간단하고,,, 어렵다,,,

n = int(input())
files = [input() for _ in range(n)]
pattern = ""

# zip() 함수는 동일 위치에 있는 것끼리 묶어줌! 리스트 앞에 *를 붙이면 col끼리 서로 엮어준다. ★
# zip()과 *args에 관한 더 자세한 이야기 (https://bit.ly/3t4e7Ij)
for columns in zip(*files):
    pattern += "?" if columns.count(columns[0]) < n else columns[0]
    # 각 columns에서 첫번째 columns의 문자열을 세었을 때,
    # col 개수보다 작으면(== 다른 문자가 있으면) 패턴에 "?" 추가, 아니면 해당 문자 추가

print(pattern)

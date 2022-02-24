## 명령 프롬프트

n = int(input())
filename = [list(map(str, input())) for _ in range(n)]    # 2차원 리스트 형식, input으로 들어온 문자열의 문자 하나하나를 리스트의 원소로 map
answer = filename[0]    # 기준 문자열

for j in range(len(answer)):
    check = set()     # 집합 초기화
    for i in range(n):
        check.add(filename[i][j])    # 문자열에서 같은 위치의 문자를 하나씩 집어넣기

        # 집합이 1개 이상이되면, 즉 문자열에서 같은 위치에 문자가 서로 다르면
        if len(check) != 1:
            answer[j] = "?"   # 기준 문자열 업데이트

print("".join(answer))    # 정답은 문자열로 출력

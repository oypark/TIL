## 스위치 켜고 끄기

n = int(input())    #스위치 개수
status = list(map(int, input().split()))    #스위치 상태
s = int(input())    #학생 수
student = [tuple(map(int, input().split())) for _ in range(s)]
on_off = {1:0, 0:1}    #on-off

for (sex, switch) in student:
    # 남자인 경우
    if sex == 1:
        share = n // switch
        for i in range(1, share + 1):
            switch_idx = switch * i -1
            status[switch_idx] = on_off[status[switch_idx]]

    # 여자인 경우
    if sex == 2:
        min_dis = min(abs(1-switch), abs(n-switch))    #더 가까운 쪽 거리
        for dis in range(min_dis + 1):
            switch_idx = switch - 1
            if dis == 0:
                status[switch_idx] = on_off[status[switch_idx]]
            else:
                left = status[switch_idx - dis]
                right = status[switch_idx + dis]
                if left == right:
                    status[switch_idx - dis] = on_off[left]
                    status[switch_idx + dis] = on_off[right]
                else:
                    break

for i, s in enumerate(status):
    if (i != 0) and (i % 20 == 0):
        print()
    print(s, end=' ')


## dictinary 사용에서 key값이 같으면 value만 교체된다는 걸 간과하고 있었음..
## 계속 시간을 신경쓰느라 머릿속으로만 계산하고 있음.. 일단 코드 돌려보고 안되면 고치도록!
## 출력 방식에서 해멨음... <- 앞으로 주의!!!
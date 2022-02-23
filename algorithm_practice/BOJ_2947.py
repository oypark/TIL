numbers = list(map(int, input().split()))    # 1부터 5까지의 숫자
one_idx = numbers.index(1)
answer = sorted(numbers)

# 1의 인덱스 숫자만큼 (1이 첫번째에 와야하기 때문에!) for문 돌림
for _ in range(4):
    for i in range(4):

        # numbers가 정렬되지 않았으면
        if numbers != answer:
            
            # 앞에 있는 숫자가 더 크면
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]    # 서로 위치 바꾸기

                for number in numbers:
                    print(number, end=" ")    # 위치 변경한 numbers 출력
                print()

        # numbers가 정렬 되었으면
        else:
            break    # for문 종료


## 매커니즘은 금방 잡았는데 구현에 시간이 좀 걸렸다. 조금 더 연습 해야할듯..!
## 효율성을 생각하다가 edge case를 놓치는 경우가 계속 생김...
## 일단은 생각나는 대로 구현하고, 효율성은 그 다음에 코드를 한 번 더 생각해보자.
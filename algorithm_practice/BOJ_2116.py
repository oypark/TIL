## 주사위 쌓기
# ======================================================================
# 주사위를 아래부터 주사위1, 주사위2, 주사위3... 이런식으로 쌓을 수 있는데
# 주사위 1은 아무렇게나 놓아도 되지만 그 다음부터는 제일 윗면에 있는 숫자와
# 동일한 숫자가 가장 아랫면에 가도록 쌓아야함! 최종적으로 만들어지는
# 긴 사각기둥 4개의 옆면 중 하나의 합을 최댓값으로 만드는 프로그램 작성
# ======================================================================

n = int(input())
dices = [list(map(int, input().split())) for _ in range(n)]

def dice_max(dices, bottom):
    max_sum = 0
    for dice in dices:
        idx = dice.index(bottom)   #bottom 인덱스 반환

        if (idx == 0) | (idx == 5):
            if idx == 0:
                top = dice[5]
            else:
                top = dice[0]
            max_sum += max(dice[1:5])

        elif (idx == 1) | (idx == 3):
            if idx == 1:
                top = dice[3]
            else:
                top = dice[1]
            max_sum += max(dice[0], dice[2], dice[4], dice[5])

        elif (idx == 2) | (idx == 4):
            if idx == 2:
                top = dice[4]
            else:
                top = dice[2]
            max_sum += max(dice[0], dice[1], dice[3], dice[5])

        bottom = top

    return max_sum


answer = 0
for bottom in dices[0]:
    new_sum = dice_max(dices, bottom)
    if new_sum > answer:
        answer = new_sum

print(answer)


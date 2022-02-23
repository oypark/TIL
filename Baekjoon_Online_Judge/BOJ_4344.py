c = int(input())

for c in range(c):
    case = list(map(int, input().split()))
    number = case[0]
    scores = case[1:]
    mean_score = sum(scores)/number
    count = 0
    for score in scores:
        if score > mean_score:
            count += 1
    print("{:.3f}%".format(count/number*100))
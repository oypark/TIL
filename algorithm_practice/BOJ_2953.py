for i in range(5):
    score = sum(map(int, input().split()))
    if i == 0:
        max_score = score
        max_person = i + 1
    else:
        if score > max_score:
            max_score = score
            max_person = i + 1

print(max_person, max_score)
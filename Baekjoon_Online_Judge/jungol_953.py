players = input().split()

foul = {}
for player in players:
    if player not in foul:
        foul[player] = 1
    else:
        foul[player] += 1

min_foul = min(foul.values())
for key, value in foul.items():
    if value == min_foul:
        print(key)

print(min_foul)
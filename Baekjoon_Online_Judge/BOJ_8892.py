words = [[], []]
for case in range(int(input())):
    for line in range(int(input())):
        words[case].append(input())

    i, j = 0, 1
    while i < len(words[case]):
        while j < (len(words[case])):
            word_comb = words[case][i] + words[case][j]
            comb_revs = words[case][j] + words[case][i]
            print(word_comb)
            if word_comb[::-1] == word_comb:
                print(word_comb)
                break
            elif comb_revs[::-1] == comb_revs:
                print(comb_revs)
                break
            else:
                j += 1
                if i == len(words[case])-1:
                    print(0)
        i += 1
        j = i + 1

## 완성은 못했지만, cheat sheet 보니 확인하려는 매커니즘은 같음!!
## 내일 작심해서 cheat sheet 안보고 스스로 다시 도전★


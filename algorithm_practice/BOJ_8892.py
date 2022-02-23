## 기존 풀이 (미완성)

# words = [[], []]
# for case in range(int(input())):
#     for line in range(int(input())):
#         words[case].append(input())

#     i, j = 0, 1
#     while i < len(words[case]):
#         while j < (len(words[case])):
#             word_comb = words[case][i] + words[case][j]
#             comb_revs = words[case][j] + words[case][i]
#             print(word_comb)
#             if word_comb[::-1] == word_comb:
#                 print(word_comb)
#                 break
#             elif comb_revs[::-1] == comb_revs:
#                 print(comb_revs)
#                 break
#             else:
#                 j += 1
#                 if i == len(words[case])-1:
#                     print(0)
#         i += 1
#         j = i + 1


# 완성은 못했지만, cheat sheet 보니 확인하려는 매커니즘은 같음!!
# 내일 작심해서 cheat sheet 안보고 스스로 다시 도전★



## 새로운 풀이 (완성)

def find_palindrome(k, words):

    # 0번부터 k-2번 인덱스까지 돌리기 (k가 5면 0,1,2,3번 돌리기)
    for i in range(k - 1):
        # 1번부터 k-1번 인덱스까지 돌리기 (k가 5면 1,2,3,4번 돌리기) => 서로다른 조합으로 중복되지 않게!
        for j in range(i + 1, k):
        # if i != j:     # 이렇게 하면 k가 1일 때 팰린드롬이 만들어져도 0 나옴
            pw1 = words[i] + words[j]     # i + j 조합
            if pw1 == pw1[::-1]:
                return pw1
            
            pw2 = words[j] + words[i]     # j + i 조합
            if pw2 == pw2[::-1]:
                return pw2
            
    return 0    # 위에서 return 없으면 0 출력(위에서 return이 생기면 그대로 함수 종료!)
 
t = int(input())    # test_case 개수

for _ in range(t):
    k = int(input())    # 단어 수
    words = [input() for _ in range(k)]

    palindrome = find_palindrome(k, words)   # 팰린드롬 찾아내는 함수 호출
    print(palindrome)



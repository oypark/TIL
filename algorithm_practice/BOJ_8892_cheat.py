## 강사님 코드

def find_palindrome(k, words):
    # words에 있는 단어 들을 두 개씩 조합하는 경우의 수
    for i in range(k - 1):
        for j in range(i + 1, k):
            password1 = words[i] + words[j] # 단어1 + 단어2
            if password1 == password1[::-1]: # 팰린드롬인가?
                return password1

            password2 = words[j] + words[i] # 단어2 + 단어1
            if password2 == password2[::-1]: # 팰린드롬인가?
                return password2

    return 0 # 팰린드 


for _ in range(int(input())):
    k = int(input())

    # list comprehension 통해서 k개의 단어 words라는 리스트에 할당
    words = [input() for _ in range(k)]

    print(find_palindrome(k, words))
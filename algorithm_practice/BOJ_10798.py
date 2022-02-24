## 세로 읽기

letters = [input() for _ in range(5)]
max_len = max(len(letter) for letter in letters)
pattern = ""

# max_len 보다 짧은 문자열의 빈칸을 .으로 채워주기
for i, letter in enumerate(letters):
    letter_len = len(letter)
    if letter_len != max_len:
        letters[i] = letter + "." * (max_len - letter_len)

# letters를 세로로 읽어서 문자열로 pattern에 저장
for vertical in zip(*letters):
    pattern += "".join(vertical)

# 채웠던 . 삭제 후 반환
print(pattern.replace(".",""))



## 다른 풀이

words = [input() for _ in range(5)]
max_len = max(len(word) for word in words)

for i in range(max_len):
    for word in words:
        # 길이가 max_len보다 짧은 문자열은 i를 len(word)-1 까지만 반복!
        if i < len(word):
            print(word[i], end="")
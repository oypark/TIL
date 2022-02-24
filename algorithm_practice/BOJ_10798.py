## 세로 읽기

letters = [input() for _ in range(5)]
max_len = max(len(letter) for letter in letters)
pattern = ""

for i, letter in enumerate(letters):
    letter_len = len(letter)
    if letter_len != max_len:
        letters[i] = letter + "." * (max_len - letter_len)

for vertical in zip(*letters):
    pattern += "".join(vertical)

print(pattern.replace(".",""))


## 다른 풀이

words = [input() for _ in range(5)]
max_len = max(len(word) for word in words)

for i in range(max_len):
    for word in words:
        # 길이가 max_len보다 짧은 문자열은 i를 len(word)-1 까지만 반복!
        if i < len(word):
            print(word[i], end="")
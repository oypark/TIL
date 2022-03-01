## 다이얼

alphabet_time = {
    'A':3, 'B':3, 'C':3,
    'D':4, 'E':4, 'F':4,
    'G':5, 'H':5, 'I':5,
    'J':6, 'K':6, 'L':6,
    'M':7, 'N':7, 'O':7,
    'P':8, 'Q':8, 'R':8, 'S':8,
    'T':9, 'U':9, 'V':9,
    'W':10, 'X':10, 'Y':10, 'Z':10,
}

time = 0
for alphabet in input():
    time += alphabet_time[alphabet]

print(time)


## 다른 풀이 - 시간 동일!

dial = {
    "ABC": 3,
    "DEF": 4,
    "GHI": 5,
    "JKL": 6,
    "MNO": 7,
    "PQRS": 8,
    "TUV": 9,
    "WXYZ": 10,
}

total = 0
for char in input():
    for key in dial:
        if char in key:
            total += dial[key]
print(total)
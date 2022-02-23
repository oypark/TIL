# 숫자 문자열과 영단어

# 강사님 풀이
# 1. 숫자 영단어 테이블을 딕셔너리로 정의
def solution(s):
    number = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

# 2. 문자열에서 영어를 숫자로 변경
    for key, value in number.items():
        s = s.replace(key, value)

# 3. 바뀐 숫자를 출력
    return int(s)


# 다른 학생 풀이 참고 - 매커니즘은 같게 생각했으나,, 코드화가 너무 어려웠다,,,, 더 연습하자!!!!

def solution(s):
    numbers = {
        "ze": ["0", 4],     # value에는 ["숫자", 영단어 길어]
        "on": ["1", 3],
        "tw": ["2", 3],
        "th": ["3", 5],
        "fo": ["4", 4],
        "fi": ["5", 4],
        "si": ["6", 3],
        "se": ["7", 5],
        "ei": ["8", 5],
        "ni": ["9", 4]
    }

    answer = ''
    i = 0

    while i < len(s):
        temp = numbers.get(s[i:i+2])    #딕셔너리에서 s의 맨앞 두글자로 key 검색
        # 숫자인 경우(key가 없다면)
        if temp == None:
            answer += s[i]    #i번째 s 그대로 answer에 넣기
            i += 1            #i 한 칸 옮기기
        # 문자열인 경우
        else:
            answer += temp[0]    #딕셔너리 value의 숫자를 answer에 넣기
            i += temp[1]         #딕셔너리 value의 영단어 길이만큼 i 옮기기

    return int(answer)


print(solution("one4seveneight"))

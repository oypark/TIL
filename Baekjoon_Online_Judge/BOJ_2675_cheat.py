for _ in range(int(input())):    # t를 이렇게 range에 넣어서 받을 수도 있다..! 할당x
    r, s = input().split()
    for char in s:
        print(char * int(r), end="")    # end=""로 해서 char가 딱 붙어서 출력되게끔!
    print()     # 이게 없으면 첫번째줄 결과값과 두번째줄 입력값이 붙어버림!
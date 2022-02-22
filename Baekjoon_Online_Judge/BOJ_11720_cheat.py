n = int(input())    #파이썬에서는 필요없지만 다른 언어도 풀수 있도록 한 것!
numbers = map(int, input())   #map에서 iterable인 문자열로 들어온 input을 하나하나 int로 바꿔서 list로 반환해줌!
print(sum(numbers))
word = input()
croa_alpha = ["c=","c-","dz=","d-","lj","nj","s=","z="]
alpha_cnt = 0

# 크로아티아 알파벳만 카운팅
for i in croa_alpha:
    cnt = word.count(i)
    alpha_cnt += cnt
    word = word.replace(i," ")

word = word.replace(" ","")
alpha_cnt += len(word)   # 1자리수 알파벳 마저 카운팅
print(alpha_cnt)
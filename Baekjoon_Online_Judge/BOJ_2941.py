word = input()
croa_alpha = ["c=","c-","dz=","d-","lj","nj","s=","z="]
alpha_cnt = 0

for i in croa_alpha:
    cnt = word.count(i)
    alpha_cnt += cnt
    word = word.replace(i," ")

word = word.replace(" ","")
alpha_cnt += len(word)
print(alpha_cnt)
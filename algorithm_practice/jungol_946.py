n = int(input())

cntry_cap = {}
for i in range(n):
    key, value = input().split()
    cntry_cap[key] = value

print(cntry_cap.get(input(), "Unknown Country"))
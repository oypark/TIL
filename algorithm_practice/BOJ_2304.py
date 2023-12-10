## 창고 다각형


n = int(input())    # 1이상 1000이하
lh_dict = {}
dist_l_list = []
dist_h_list = []

for n in range(n):
    l, h = map(int, input().split())     # 1이상 1000이하
    lh_dict[l] = h

    if n == 0:
        max_h = h
    else:
        if h > max_h:
            max_h = h

lh_dict = sorted(lh_dict.items())
l_list = [k for (k, v) in lh_dict]
h_list = [v for (k, v) in lh_dict]
dist_l_list = [l - l_list[:-1][i] for i, l in enumerate(l_list[1:])]
dist_h_list = [h - h_list[:-1][i] for i, h in enumerate(h_list[1:])]
max_h_idx = h_list.index(max_h)

sum_garage = 0

for j, h in enumerate(h_list):
    # max_h 나오기 전까지
    if j < max_h_idx:
        if j == 0:
            sum_garage += dist_l_list[j] * h
            print(j, dist_l_list[j], h)

        elif dist_h_list[j-1] >= 0:
            sum_garage += dist_l_list[j] * h
            print(j, dist_l_list[j], h)
        else:
            sum_garage += dist_l_list[j] * h_list[j-1]
            print(j, dist_l_list[j], h_list[j-1])

    elif j == max_h_idx:
        sum_garage += 1 * h
        print(j, 1, h)

    else:
        if dist_h_list[j-1] < 0:
            square = dist_l_list[j-1] * h
            print(j, dist_l_list[j-1], h)
            sum_garage += square
        else:
            square_large = (dist_l_list[j-2] + dist_l_list[j-2]) * h
            print(j, dist_l_list[j-2], dist_l_list[j-2], h, square_large)
            square_small = (dist_l_list[j-2] * h_list[j-1])
            print(j, dist_l_list[j-2], h_list[j-1], square_small)
            sum_garage += square_large
            sum_garage -= square_small
            

print(sum_garage)

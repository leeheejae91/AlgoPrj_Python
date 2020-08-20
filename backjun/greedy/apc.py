from itertools import combinations

n, l, k = [int(i) for i in str(raw_input()).split()]

point_arr = []
answer_arr = []

for _ in range(n):
    temp_arr = [int(i) for i in str(raw_input()).split()]
    if temp_arr[0] <= l and temp_arr[1] <= l:
        point_arr.append(140)
    elif temp_arr[0] <= l <= temp_arr[1]:
        point_arr.append(100)
    else:
        point_arr.append(0)

count_140 = point_arr.count(140)
count_100 = point_arr.count(100)
count_0 = point_arr.count(0)

point = 0
if count_140 >= k:
    point += (k * 140)
else:
    point += (count_140 * 140)
    k -= count_140

    if count_100 >= k:
        point += (k * 100)
    else:
        point += (count_100 * 100)

print(point)

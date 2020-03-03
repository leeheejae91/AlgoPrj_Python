alpha = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

target = list(input())
cur = 0
count = 0
count_arr = []
for i in target:
    count_arr.append(min(alpha.index(i), len(alpha) - alpha.index(i)))

while True:
    count += count_arr[cur]
    count_arr[cur] = 0

    if sum(count_arr) == 0:
        break

    move_arr = []
    # 움직일 칸 수 구하기
    for i in range(len(count_arr)):
        if count_arr[i] == 0:
            move_arr.append(99)
        else:
            move_arr.append(min(abs(i - cur), abs(len(count_arr) - i + cur)))

    # 최소 움직일 idx 구하기
    min_idx = 0
    for i in range(len(move_arr)):
        if move_arr[i] != 99 and move_arr[min_idx] > move_arr[i]:
            min_idx = i

    cur = min_idx
    count += move_arr[min_idx]

print(count)

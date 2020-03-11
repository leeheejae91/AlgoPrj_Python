# 24	24
brown = 8
red = 1
red_arr = []
ans_arr = []

if red == 1:
    red_arr.append(1)
else :
    for i in range(1, int(red/2) +1):
        if red % i == 0:
            red_arr.append(int(i))

for i in red_arr:
    brown_y = i+2
    brown_x = int(red/i) + 2

    if brown_x * brown_y - red == brown and brown_x >= brown_y:
        ans_arr.append(brown_x)
        ans_arr.append(brown_y)
        break

print(ans_arr)


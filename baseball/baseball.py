# baseball	return
# [[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]	2
input_arr = [[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]
answer = []

for i in range(100, 1000):
    i_str = str(i)
    flag = True

    if i_str[0] == '0' or i_str[1] == '0' or i_str[2] == '0':
        continue
    if i_str[0] == i_str[1] or i_str[1] == i_str[2] or i_str[2] == i_str[0]:
        continue

    for j in input_arr:
        cnt_s = 0
        cnt_b = 0

        q_num = str(j[0])
        q_strike = j[1]
        q_ball = j[2]

        for idx_i in range(len(i_str)):
            for idx_q in range(len(q_num)):
                if idx_i == idx_q and i_str[idx_i] == q_num[idx_q]:
                    cnt_s += 1
                elif idx_i != idx_q and i_str[idx_i] == q_num[idx_q]:
                    cnt_b += 1

        if cnt_s != q_strike or cnt_b != q_ball:
            flag = False
            break

    if flag:
        answer.append(i_str)

print(answer)



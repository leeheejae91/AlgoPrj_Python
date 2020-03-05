# baseball	return
# [[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]	2
temp_arr = ['1','2','3','4','5','6','7','8','9']
input_arr = [[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]];


def baseball_check(q, input_data):
    q_num = str(q[0])
    q_strike = q[1]
    q_ball = q[2]

    cnt_strike = 0
    cnt_ball = 0

    # 카운트
    for i in range(len(q_num)):
        for j in range(len(input_data)):
            if i == j and q_num[i] == input_data[j]:
                cnt_strike += 1
            elif i != j and q_num[i] == input_data[j]:
                cnt_ball += 1

    if cnt_strike == 0 and cnt_ball == 0:
        return False
    else:
        return q_strike == cnt_strike and q_ball == cnt_ball


def make_arr():
    temp_list = []
    '''
    for i in range(len(temp_arr)):
        for j in range(len(temp_arr)):
            if j != i:
                for z in range(len(temp_arr)):
                    if z != i and z != j:
                        temp_list.append(temp_arr[i] + temp_arr[j] + temp_arr[z])
    '''

    for i in range(100,999):
        ttemp_arr = str(i)

        if ttemp_arr[0] == '0' or ttemp_arr[1] == '0' or ttemp_arr[2] == '0':
            continue
        if ttemp_arr[0] == ttemp_arr[1] or ttemp_arr[1] == ttemp_arr[2] or ttemp_arr[2] == ttemp_arr[0]:
            continue
        temp_list.append(ttemp_arr)
    return temp_list


baseball_list = make_arr()
idx = 0

while idx < len(baseball_list):
    check_flag = True
    for j in input_arr:
        check_flag = baseball_check(j, baseball_list[idx])
        if not check_flag:
            break

    if not check_flag:
        baseball_list.pop(idx)
    else:
        idx += 1

print(baseball_list)

def solution(key, lock):
    answer = True

    # 회전
    key = rotate(key)

    # 맵 만들기
    lock_map = []
    map_len = len(lock) + (len(key) - 1) * 2
    for i in range(map_len):
        if i < len(key)-1 or i > len(key) + len(lock) - 2:
            temp_arr = [0] * map_len
        else:
            temp_arr = [0] * (len(key)-1) + lock[i - len(key) + 1] + [0] * (len(key)-1)
        lock_map.append(temp_arr)

    for i in range(0, map_len - len(key) + 1):
        for j in range(0, map_len - len(key) + 1):
            print(get_sub_map(lock_map, key, i, j, lock))

    return answer


def rotate(key):
    key_len = len(key)
    rotate_arr = []

    for i in range(key_len):
        temp_arr = []
        for j in range(key_len-1, -1, -1):
            temp_arr.append(key[j][i])
        rotate_arr.append(temp_arr)

    return rotate_arr


def check_sum(map_arr, key, lock):
    k = len(key)
    l = len(lock)

    temp_sum = 0
    for i in range(k-1, k + l):
        temp_sum = temp_sum + sum(map_arr[i][k-1:k+l])

    return temp_sum == len(key) * len(key)


def get_sub_map(map_arr, key, i, j, lock):
    temp_map = []
    for xx in map_arr:
        temp_map.append(xx)

    for x in range(i, i + len(key)):
        for y in range(j, j + len(key)):
            temp_map[x][y] = temp_map[x][y] + key[x-len(key)-1][y-len(key)-1]

    return check_sum(temp_map, key, lock)


key_input = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock_input = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

solution(key_input,lock_input)
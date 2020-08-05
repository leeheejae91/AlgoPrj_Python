# -*- coding: utf-8 -*-
import copy


def solution(key, lock):
    answer = False
    key_arr = [key]
    for i in range(3):
        key_arr.append(rotate(key))

    # 맵 만들기
    lock_map = []
    map_len = len(lock) + (len(key) - 1) * 2
    for i in range(map_len):
        if i < len(key)-1 or i > len(key) + len(lock) - 2:
            temp_arr = [0] * map_len
        else:
            temp_arr = [0] * (len(key)-1) + lock[i - len(key) + 1] + [0] * (len(key)-1)
        lock_map.append(temp_arr)

    for temp_key in key_arr:
        for i in range(0, map_len - len(temp_key) + 1):
            for j in range(0, map_len - len(temp_key) + 1):
                if get_sub_map(lock_map, temp_key, i, j, lock):
                    return True

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

    for i in range(k-1, k + l -1):
        temp_arr = map_arr[i][k-1:k+l-1]
        for j in temp_arr:
            if j != 1:
                return False

    return True


def get_sub_map(map_arr, key, i, j, lock):
    temp_map = copy.deepcopy(map_arr)

    for x in range(i, i + len(key)):
        for y in range(j, j + len(key)):
            temp_map[x][y] = temp_map[x][y] + key[x-i][y-j]

    return check_sum(temp_map, key, lock)


key_input = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock_input = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

print(solution(key_input,lock_input))
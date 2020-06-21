from itertools import permutations

input_data = [3,3,3,2,2,2]


def solution(nums):
    answer = 0
    temp_len = len(list(set(list(nums))))
    if int(len(nums)/2) > temp_len:
        answer = temp_len
    else :
        answer = int(len(nums)/2)
    return answer


solution(input_data)
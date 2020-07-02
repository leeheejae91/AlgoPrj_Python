def solution(arr1, arr2):
    answer = []

    for x in range(len(arr1)):
        sub_arr = []
        for y in range(len(arr2[0])):
            t_arr = []
            for k in arr2:
                t_arr.append(k[y])

            sub_arr.append(sum([arr1[x][z] * t_arr[z] for z in range(len(arr1[x]))]))
        answer.append(sub_arr)

    return answer


temp_arr1 = [[2, 3, 2],
             [4, 2, 4],
             [3, 1, 4]]
temp_arr2 = [[5, 4, 3],
             [2, 4, 1],
             [3, 1, 1]]

solution(temp_arr1,temp_arr2)
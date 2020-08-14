def solution(triangle):
    df = [[triangle[0][0]]]

    for i in range(1, len(triangle)):
        temp_arr = []
        for j in range(len(triangle[i])-1):
            if len(temp_arr) == 0:
                temp_arr.append(df[i - 1][j] + triangle[i][j])
                temp_arr.append(df[i - 1][j] + triangle[i][j+1])
            else:
                if temp_arr[j] < df[i - 1][j] + triangle[i][j]:
                    temp_arr[j] = df[i - 1][j] + triangle[i][j]
                temp_arr.append(df[i - 1][j] + triangle[i][j + 1])
        df.append(temp_arr)
    return max(df[len(triangle) - 1])


tri = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print solution(tri)

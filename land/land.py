input_map = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]


def solution(land):
    answer = 0
    for i in range(len(land)):
        if i == 0 :
            continue

        for j in range(len(land[i])):
            land[i][j] = land[i][j] + max([ land[i-1][k] if k != j else 0 for k in range(len(land[i]))])

    return max(land[len(land)-1])


solution(input_map)
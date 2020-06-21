input_num = 15


def solution(n):
    i_bin = bin(n)
    cnt = sum([int(i) for i in i_bin[2:]])

    while True:
        n = n+1
        temp_bin = bin(n)

        if cnt == sum([int(i) for i in temp_bin[2:]]):
            break

    return n


print solution(input_num)
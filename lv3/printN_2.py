def solution(N, number):
    answer = -1
    data_map = [[], [N]]
    print(data_map)
    for i in range(2, 9):
        data_map.append([int(str(N) * i)])

        for j in range(1, int(i/2) + 1):
            first_arr = data_map[j]
            second_arr = data_map[i-j]

            for x in first_arr:
                for y in second_arr:
                    if x + y not in data_map[i]:
                        data_map[i].append(x + y)
                    if x * y not in data_map[i]:
                        data_map[i].append(x * y)

                    if x - y > 0 and x - y not in data_map[i]:
                        data_map[i].append(x - y)
                    if y - x > 0 and x - y not in data_map[i]:
                        data_map[i].append(y - x)
                    if x != 0 and int(y/x) not in data_map[i]:
                        data_map[i].append(int(y / x))
                    if y != 0 and int(x/y) not in data_map[i]:
                        data_map[i].append(int(x / y))

        if number in data_map[i]:
            answer = i
            return answer

    return answer


N = 5
number = 12
solution(N, number)




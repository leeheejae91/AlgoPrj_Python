def solution(N, number):
    answer = -1
    for i in range(1, 9):
        if number in foo(N, i, 11):
            answer = i
            print(answer)
            return answer

    return answer


def foo(N, count, number):
    temp_list = []
    if count == 1:
        temp_list.append(N)
    else:
        for k in range(1, int(count/2) + 1):
            for i in foo(N, count-k, number):
                for j in foo(N, k, number):
                    temp_list.append(i + j)
                    temp_list.append(i * j)

                    if j - i > 0:
                        temp_list.append(j - i)
                    if i - j > 0:
                        temp_list.append(i - j)

                    if j != 0:
                        temp_list.append(int(i // j))
                    if i != 0:
                        temp_list.append(int(j // i))

                    temp_list.append(int(str(i) + str(j)))

    '''
    if count != 1:
        print(count, temp_list)
    '''

    return temp_list

'''
N	number	return
5	12	4
2	11	3

N = 5
number = 12

N = 2
number = 11
'''
N = 5
number = 31168
solution(N, number)




def solution(numbers, hand):
    keypad = [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9'],
        ['*', '0', '#'],
    ]

    left = (3, 0)
    right = (3, 2)
    answer = []

    for i in numbers:
        if i in [1, 4, 7]:
            left = (int(i/3), 0)
            answer.append('L')
        elif i in [3, 6, 9]:
            right = (int((i-1)/3), 2)
            answer.append('R')
        else:
            target = str(i)
            target_point = (-1, -1)
            for x in range(len(keypad)):
                for y in range(len(keypad[x])):
                    if target == keypad[x][y]:
                        target_point = (x, y)
                        break

                if target_point[0] != -1:
                    break

            right_term = abs(target_point[0] - right[0]) + abs(target_point[1] - right[1])
            left_term = abs(target_point[0] - left[0]) + abs(target_point[1] - left[1])

            if right_term > left_term:
                left = target_point
                answer.append('L')
            elif right_term < left_term:
                right = target_point
                answer.append('R')
            else:
                if hand == 'right':
                    right = target_point
                    answer.append('R')
                else:
                    left = target_point
                    answer.append('L')

    return ''.join(answer)


print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0],	"right"))

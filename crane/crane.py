b = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
m = [1, 5, 3, 5, 1, 2, 1, 4]


def get_top(board, line):
    line = line - 1
    for i in range(len(board)):
        if board[i][line] != 0:
            result = board[i][line]
            board[i][line] = 0
            return result
    return 0


def solution(board, moves):
    queue = []
    answer = 0

    for i in moves:
        topValue = get_top(board, i)
        if topValue == 0:
            continue
        elif (0 if len(queue) == 0 else queue[len(queue) - 1]) == topValue:
            queue.pop()
            answer = answer + 2
        else:
            queue.append(topValue)
    return answer


print(solution(b, m))

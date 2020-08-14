def solution(begin, target, words):
    visited = []
    rank_map = [[begin]]

    answer = 0
    find_flag = False
    for queue in rank_map:
        temp_arr = []
        for j in range(len(queue)):
            x = queue[j]

            if x not in visited:
                for i in words:
                    if can_change(x, i) and i not in visited and i not in queue and i not in temp_arr:
                        temp_arr.append(i)
            visited.append(x)

        if len(temp_arr) != 0:
            rank_map.append(temp_arr)

        if target in temp_arr:
            answer += 1
            find_flag = True
            break

    if find_flag:
        answer = len(rank_map)-1
    return answer


def can_change(word1, word2):
    count = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            count += 1

    if count == 1:
        return True
    else:
        return False


input1 = ['hot', 'dot', 'dog', 'lot', 'log']
input2 = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']
print(solution('hit', 'cog', input2))

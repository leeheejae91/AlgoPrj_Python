from itertools import combinations
from itertools import permutations


def solution(user_id, banned_id):
    com_arr = []
    for i in banned_id:
        for j in user_id:
            if len(i) == len(j):
                result = True

                for k in range(len(i)):
                    if i[k] != '*' and i[k] != j[k]:
                        result = False
                        break

                if result and j not in com_arr:
                    com_arr.append(j)

    count = 0
    answer = []
    for i in list(permutations(com_arr, len(banned_id))):
        if check_answer(i, banned_id):
            answer.append(i)
            count += 1

    if count != 2:
        return count/2
    else:
        return count


def check_answer(answer, banned_id):
    for i in range(len(answer)):
        if len(answer[i]) != len(banned_id[i]):
            return False

    for i in range(len(answer)):
        for j in range(len(answer[i])):
            if banned_id[i][j] != '*' and banned_id[i][j] != answer[i][j]:
                return False

    return True




print solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"])

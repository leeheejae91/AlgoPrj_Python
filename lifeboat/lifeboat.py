p = [70, 50, 80, 50, 30]
l = 100


def sol(people, limit):
    answer = 0
    people = sorted(people, reverse=True)

    i = 0
    j = len(people)-1

    while j >= i:
        if people[i] + people[j] <= limit:
            i = i + 1
            j = j - 1
        else :
            i = i + 1

        answer += 1

    return answer


print(sol(p, l))

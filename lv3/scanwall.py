import itertools
import copy


def solution(n, weak, dist):
    dist.sort(reverse=True)

    for i in range(len(dist)):
        # 투입 인원 순열
        for p in list(itertools.permutations(dist[0:i+1])):
            temp_weak = copy.deepcopy(weak)
            check_map(n, temp_weak, p)

    answer = 0
    return answer


def check_map(n, weak, dist):
    for _ in range(len(weak)):
        temp_val = weak.pop(0)
        weak.append(temp_val + n)

        idx = 0
        cnt = 0

        for i in dist:
            min_weak = weak[idx]
            max_weak = weak[idx] + i

            for j in range(idx, len(weak)):
                if min_weak <= j <= max_weak:
                    cnt += 1
                else:
                    idx = j
                    break

        if cnt == len(weak):
            return True

    return False



solution(12, [1, 5, 6, 10], [1, 2, 3, 4])

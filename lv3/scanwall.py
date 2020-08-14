# -*- coding: utf-8 -*-
"""
1. 제일 먼거리 부터 갈 수 있도록 dist를 정렬한다.
2. 점검 순서도 중요하므로 순열로 dist를 조합한다.
3. 해당 조합에 따라 weak가 범위에 포함되는지 count 한다.
4. weak의 시작점이 변경가능하므로 회전 할 수 있도록 + n 한다.
5. 빈 weak 없이 count 후 일치시 return
"""

import itertools
import copy


def solution(n, weak, dist):
    dist.sort(reverse=True)

    answer = -1
    for i in range(len(dist)):
        # 투입 인원 순열
        for p in list(itertools.permutations(dist[0:i + 1])):
            temp_weak = copy.deepcopy(weak)
            if check_map(n, temp_weak, p):
                return len(dist[0:i+1])

    return answer


def check_map(n, weak, dist):
    for _ in range(len(weak)):
        idx = 0
        cnt = 0

        for i in dist:
            min_weak = weak[idx]
            max_weak = weak[idx] + i

            for j in range(idx, len(weak)):
                if min_weak <= weak[j] <= max_weak:
                    cnt += 1
                else:
                    idx = j
                    break

        if cnt == len(weak):
            return True

        temp_val = weak.pop(0)
        weak.append(temp_val + n)

    return False


print solution(12, [1, 5, 6, 10], [1, 2, 3, 4])

def solution(n, build_frame):
    answer = [[]]
    build_map = [[-1] * (n + 1) for _ in range(n + 1)]

    for i in build_frame:
        y, x, w, k = i[0], i[1], i[2], i[3]

        # 설치
        if k == 1 and can_insert(build_map, x, y, w):
            build_map[x][y] = w
        # 삭제
        elif k == 0 and can_delete(build_map, x, y, w):
            build_map[x][y] = -1

    print_map(build_map)

    return answer


def print_map(build_map):
    for i in range(len(build_map)-1, -1, -1):
        print(build_map[i])


def can_insert(build_map, x, y, w):
    # 기둥 설치
    result = False
    if w == 0:
        if x == 0 or (x > 0 and build_map[x - 1][y] == 0):
            result = True
        elif (y > 0 and build_map[x][y-1] == 1) or (y < len(build_map)-1 and build_map[x][y+1] == 1):
            result = True
    # 보 설치
    elif w == 1:
        # 설치 가능 범위
        if x > 0 and y < len(build_map)-1:
            # 조건
            # 양 끝이 기둥인 경우
            if build_map[x - 1][y] == 0 or build_map[x - 1][y + 1] == 0:
                result = True
            # 양 끝이 보인 경우
            elif y > 0 and build_map[x][y+1] == 1 and build_map[x][y-1] == 1:
                result = True

    return result


def can_delete(build_map, x, y, w):
    # 기둥 삭제
    result = True
    if w == 0:
        if x < len(build_map)-1:

            # 위가 기둥인 경우
            if build_map[x+1][y] == 0:
                # 양 옆 중 하나가 보면 삭제가능
                if (y > 0 and build_map[x+1][y-1] != 1) and (x < len(build_map) -1 and build_map[x+1][y+1] == 1):
                    result = False
            # 왼쪽 위가 보인 경우
            if y > 0 and build_map[x+1][y-1] == 1:
                if build_map[x][y-1] != 0:
                    result = False
            # 위가 보인 경우
            if build_map[x + 1][y] == 1:
                if y < len(build_map)-1 and build_map[x][y+1] != 0:
                    result = False
    # 보 삭제
    elif w == 1:
        # 오른쪽이 기둥인 경우
        if y < len(build_map)-1 and build_map[x][y+1] == 0:
            # 밑에 기둥이 있으면 삭제 가능
            if x > 0 and build_map[x-1][y+1] != 0:
                result = False
        # 양 옆이 보인 경우
        if 0 < y < len(build_map) - 1 and build_map[x][y - 1] == 1 and build_map[x][y + 1] == 1:
            if build_map[x-1][y-1] != 0 or build_map[x-1][y] != 0:
                result = False
            if build_map[x-1][y+1] != 0 or build_map[x-1][y+2] != 0:
                result = False

    return result



solution(5,
         [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1],
          [3, 2, 1, 1]])

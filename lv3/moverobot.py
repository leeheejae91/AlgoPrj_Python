# -*- coding: utf-8 -*-
"""
1. 회전이나 이동이 가능한지 검사
2. stack에 로봇 상태 저장
3. 이동이 불가할 경우 이전 상태로 가서 진행 (dfs?)

"""


class robot:

    def __init__(self):
        self.left = [0, 0]
        self.right = [0, 1]
        self.dist = 0

    def get_loc(self):
        return [self.left, self.right]

    def set_loc(self, loc):
        self.left = loc[0]
        self.right = loc[1]


def solution(board):
    cur_robot = robot()
    que = [cur_robot.get_loc()]
    visited = [cur_robot.get_loc()]
    n = len(board)-1

    while que:
        cur_robot.set_loc(que.pop(0))

        if [n, n] in cur_robot.get_loc():
            break
        elif cur_robot.get_loc() not in visited:
            visited.append(cur_robot.get_loc())
            que.extend(find_path(board, cur_robot))
    answer = 0
    return answer


def find_path():
    temp_path = []

    return temp_path


def check_robot(robot, n):
    if [n, n] in robot:
        return True
    else:
        return False


print solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]])

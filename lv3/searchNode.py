def solution(nodeinfo):
    num = 1
    for i in nodeinfo:
        i.append(num)
        num += 1
    nodeinfo.sort(key=lambda x: x[0])

    answer_ver = []
    preorder_find_node(answer_ver, nodeinfo)
    answer = [[i[2] for i in answer_ver]]

    answer_ver = []
    postorder_find_node(answer_ver, nodeinfo)
    answer.append([i[2] for i in answer_ver])

    return answer


def preorder_find_node(answer_ver, nodeinfo):
    if len(nodeinfo) == 0:
        return
    elif len(nodeinfo) == 1:
        answer_ver.append(nodeinfo[0])
        return

    max_ver = max(nodeinfo, key=lambda x: x[1])

    for i in range(len(nodeinfo)):
        if nodeinfo[i] == max_ver:
            answer_ver.append(max_ver)
            nodeleft = nodeinfo[0:i]
            preorder_find_node(answer_ver, nodeleft)

            noderight = nodeinfo[i + 1:len(nodeinfo)]
            preorder_find_node(answer_ver, noderight)
            break


def postorder_find_node(answer_ver, nodeinfo):
    if len(nodeinfo) == 0:
        return
    elif len(nodeinfo) == 1:
        answer_ver.append(nodeinfo[0])
        return

    max_ver = max(nodeinfo, key=lambda x: x[1])

    for i in range(len(nodeinfo)):
        if nodeinfo[i] == max_ver:
            nodeleft = nodeinfo[0:i]
            postorder_find_node(answer_ver, nodeleft)

            noderight = nodeinfo[i + 1:len(nodeinfo)]
            postorder_find_node(answer_ver, noderight)
            answer_ver.append(max_ver)
            break


print solution([[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]])

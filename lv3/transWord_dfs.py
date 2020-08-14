def bfs(begin, target, words, visited):
    answer = 0
    stacks = [begin]

    while stacks:
        # 스택을 활용한 bfs 구현
        stack = stacks.pop()

        if stack == target:
            return answer

        for w in range(0, len(words)):
            # 조건 1. 한 개의 알파벳만 다른 경우
            if len([i for i in range(0, len(words[w])) if words[w][i] != stack[i]]) == 1:

                if visited[w] != 0:
                    continue

                visited[w] = 1

                # stack에 추가
                stacks.append(words[w])

        # depth +
        answer += 1
    return answer


def solution(begin, target, words):
    # 조건 2. words에 있는 단어로만 변환할 수 있습니다.
    if target not in words:
        return 0

    visited = [0 for i in words]

    return bfs(begin, target, words, visited)


input1 = ['hot', 'dot', 'dog', 'lot', 'log']
input2 = ['dot', 'hot', 'dog', 'lot', 'log', 'cog']
print(solution('hit', 'cog', input2))
## (()())()
input_str = list(input())


def recur_change(w):
    u = []
    v = []

    if len(w) == 0:
        return []

    while True:
        if len(w) == 0:
            break

        u.append(w.pop(0))

        if u.count('(') == u.count(')'):
            v = w
            break

    # 올바른 문자인지 검사
    if check_valid(u):
        return u + recur_change(v)
    else:
        result = ['(']
        result += recur_change(v)
        result.append(')')
        # 앞뒤 제거
        u.pop()
        u.pop(0)

        # 방향 뒤집어서 출력
        u_reverse = [')' if i == '(' else '(' for i in u]
        result += u_reverse

        return result


def check_valid(u):
    stack = []
    for i in u:
        if i == '(':
            stack.append(i)
        elif i == ')' and len(stack) != 0:
            stack.pop()

    if len(stack) == 0:
        return True
    else:
        return False


print(''.join(recur_change(input_str)))

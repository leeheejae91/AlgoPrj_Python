def solution(s):
    t = list(s.lower())
    x = t.pop(0)
    t.insert(0, str(x).upper())

    for i in range(len(t)):
        if i > 0 and t[i-1] == ' ':
            x = t.pop(i)
            t.insert(i,str(x).upper())

    return ''.join(t)


input_str = '3people unFollowed me'

solution(input_str)
def solution(n):
    if n == 0 : return 0
    elif n == 1 : return 1
    else:
        result = 0
        a = 0
        b = 1

        for i in range(1,n):
            result = a + b
            a = b
            b = result

        return result


solution(5)
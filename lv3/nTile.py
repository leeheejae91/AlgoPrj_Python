def solution(x):
    a, b, c = 1, 2, 0
    for i in range(3, x + 1):
        c = a + b
        a = b
        b = c

    return c % 1000000007

n = 100
print(solution(n))


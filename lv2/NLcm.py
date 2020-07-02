def gcd(a, b):
    if a < b:
        a, b = b, a

    while b != 0:
        a, b = b, a % b

    return a


def lcm(a, b):
    return (a * b) / gcd(a, b)


def solution(arr):
    temp_val = lcm(arr[0], arr[1])
    for i in range(2, len(arr)):
        temp_val = lcm(temp_val, arr[i])

    return int(temp_val)


input_arr = [2, 6, 8, 14]
solution(input_arr)

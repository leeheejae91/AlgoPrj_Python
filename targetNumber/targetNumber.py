numbers = [0,1,1,1,1]
target = 3
ans_arr = []


def dfs(val, depth):
    if depth == len(numbers):
        if val == target:
            ans_arr.append(val)

        return

    val1 = val + numbers[depth]
    dfs(val1, depth+1)

    val2 = val - numbers[depth]
    dfs(val2, depth+1)


dfs(0,0)
print(len(ans_arr))
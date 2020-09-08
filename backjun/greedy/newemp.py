t = input()
for _ in range(int(t)):
    n = int(input())
    arr = []
    for _ in range(n):
        temp = input().split()
        arr.append((int(temp[0]), int(temp[1])))

    arr.sort(key=lambda x: x[1])
    arr.sort(key=lambda x: x[0])

    answer = n
    for i in range(n-1):
        cur = arr[i]
        for j in range(i+1,n):
            next = arr[j]

            if cur[0] > next[0] and cur[1] > next[1]:
                answer -= 1
                break

    print(answer)

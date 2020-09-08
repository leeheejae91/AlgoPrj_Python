n = int(input())

arr = []
for _ in range(n):
    x = input().split()
    arr.append((int(x[0]), int(x[1])))

arr.sort(key=lambda x: x[0])
arr.sort(key=lambda x: x[1])

cur = arr[0]
answer = 1

for i in range(1, n):
    if cur[1] <= arr[i][0]:
        cur = arr[i]
        answer += 1

print(answer)

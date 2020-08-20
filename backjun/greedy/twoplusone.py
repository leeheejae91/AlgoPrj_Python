n = int(input())
arr = []

for _ in range(n):
    arr.append(int(input()))
n /= 3
arr.sort(reverse=True)

answer = 0
for i in range(len(arr)):
    if (i + 1) % 3 != 0:
        answer += arr[i]

print answer

for i in range(2,100,3):
    print i
n = input()
arr = sorted([int(i) for i in str(raw_input()).split()])

answer = 0
for i in range(len(arr)):
    answer += (arr[i] * (len(arr) - i))

print answer

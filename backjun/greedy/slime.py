n = input()
arr = str(input()).split()
arr = [int(i) for i in arr]

temp_sum = 0
answer = 0

for i in arr:
    answer += (i*temp_sum)
    temp_sum += i

print(answer)
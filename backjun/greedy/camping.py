L, P, V = -1, -1, -1
answer = []

while True:
    arr = str(input()).split()
    L, P, V = [int(i) for i in arr]

    if L == 0 and P == 0 and V == 0:
        break

    answer.append(int(V/P) * L + (L if int(V % P) > L else int(V % P)))

for i in range(len(answer)):
    print("Case " + str(i+1) + ": " + str(answer[i]))
k = int(input())
n_5 = int(k / 5)

if k % 5 == 0:
    print(n_5)
else:
    answer = True
    while (k - 5 * n_5) % 3 != 0:
        n_5 -= 1

        if n_5 < 0:
            answer = False
            break
    if not answer:
        print(-1)
    else:
        print(n_5 + int((k - 5 * n_5) / 3))

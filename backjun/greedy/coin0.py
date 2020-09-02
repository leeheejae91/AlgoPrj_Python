n, k = [int(i) for i in str(input()).split()]
coin = []
for _ in range(n):
    coin.append(int(input()))
coin.sort(reverse=True)

answer = 0
idx = 0
while k != 0:
    if coin[idx] <= k:
        div = int(k/coin[idx])
        k %= coin[idx]
        answer += div
    else:
        idx += 1

print(answer)
st = 4
da = [4, 10, 15]
su = [20, 5, 10]
ki = 30


def sol(stock, dates, supplies, k):
    answer = 0
    sum_stock = stock

    cur_date = 1
    pq = []

    if stock >= k:
        return 0

    idx = 0
    while idx < len(dates):
        if cur_date <= dates[idx] <= sum_stock:
            pq.append(supplies[idx])
            idx = idx + 1
        else:
            sorted(pq, reverse=True)
            cur_date = sum_stock
            sum_stock = sum_stock + pq.pop(0)
            answer = answer + 1

            if sum_stock >= k:
                return answer

    answer = answer + 1

    return answer


print(sol(st, da, su, ki))

cl = [['crow_mask', 'face'], ['blue_sunglasses', 'face'], ['smoky_makeup', 'face']]


def sol(clothes):
    dic = {}
    answer = 1

    for i in clothes:
        if i[1] not in list(dic.keys()):
            dic[i[1]] = 1
        else :
            dic[i[1]] = dic[i[1]] + 1

    for i in dic.values():
        answer = answer * (i+1)

    return answer-1


print(sol(cl))
def solution(routes):
    routes = sorted(routes, key=lambda x: x[1])
    print routes
    temp = routes[0][1]

    answer = 1

    for i in range(1,len(routes)):
        if routes[i][0] <= temp:
            temp = min(temp, routes[i][1])
        else:
            temp = routes[i][1]
            answer += 1

    return answer


route_input = [[-20, 15], [-14, -5], [-18, -13], [-5, -3]]
solution(route_input)

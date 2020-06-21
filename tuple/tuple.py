test_input = '{{4,2,3},{3},{2,3,4,1},{2,3}}'


def solution(s):
    input_arr = s.split("},")
    tuple_map = []
    answer = []
    for i in input_arr:
        i = i.replace('{','').replace('}','')
        temp_arr = i.split(",")
        tuple_map.append(temp_arr)

    tuple_map.sort(key=len)
    for i in tuple_map:
        for j in i:
            if j not in answer:
                answer.append(j)

    answer = [int(i) for i in answer]

    return answer


solution(test_input)
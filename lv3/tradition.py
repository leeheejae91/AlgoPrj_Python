import datetime

def solution(lines):
    answer = 0
    end_time_arr = []
    start_time_arr = []

    for line in lines:
        # 시작시간, 종료시간 구하기
        date, end_time, term = line.split(" ")
        YYYY, MM, DD = date.split("-")
        end_dtime, sss = end_time.split(".")
        hh, mm, ss = end_dtime.split(":")

        temp_end_dtime = datetime.datetime(int(YYYY), int(MM), int(DD), int(hh), int(mm), int(ss), int(sss)*1000)
        temp_start_dtime = temp_end_dtime - datetime.timedelta(seconds= float(term[:len(term)-1]) - 0.001)
        end_time_arr.append(temp_end_dtime)
        start_time_arr.append(temp_start_dtime)

    sec_term = (end_time_arr[len(end_time_arr)-1] - start_time_arr[0]).seconds + 2
    hit_map = sec_term * [0]

    print(start_time_arr)
    print(end_time_arr)
    for i in range(len(start_time_arr)):
        start_idx = (start_time_arr[i].second - start_time_arr[0].second)
        end_idx = (end_time_arr[i].second - start_time_arr[0].second)

        print(start_idx, end_idx)
        for j in range(start_idx, end_idx + 1):
            hit_map[j] = hit_map[j] + 1

    print(hit_map)

    return answer

input_data1 = [
    '2016-09-15 20:59:57.421 0.351s',
    '2016-09-15 20:59:58.233 1.181s',
    '2016-09-15 20:59:58.299 0.8s',
    '2016-09-15 20:59:58.688 1.04s',
    '2016-09-15 20:59:59.591 1.41s',
    '2016-09-15 21:00:00.464 1.466s',
    '2016-09-15 21:00:00.741 1.581s',
    '2016-09-15 21:00:00.748 2.31s',
    '2016-09-15 21:00:00.966 0.381s',
    '2016-09-15 21:00:02.066 2.62s'
]

input_data2 = [
'2016-09-15 01:00:04.002 2.0s',
'2016-09-15 01:00:07.000 2s'
]

solution(input_data1)


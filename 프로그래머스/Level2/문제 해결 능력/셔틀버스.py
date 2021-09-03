def solution(n, t, m, timetable):
    # 분 단위로 계산 + 시간 순서로 정렬
    timetable = sorted([int(time[:2]) * 60 + int(time[3:5]) for time in timetable])
    # 셔틀을 탈 수 있는 마지막 시간
    last = (60 * 9) + (n - 1) * t
    for i in range(n):
        if len(timetable) < m: # 한번에 탈 수 있는 max 크루 수 > 오늘 탄 크루의 수 => 무조건 마지막에 줄을 선다.
            hour, minute = last // 60, last % 60
            return '%02d:%02d' % (hour, minute)
        if i == n - 1: # 마지막 순서
            if timetable[0] <= last: # 나보다 빠른 사람이 존재함
                last= timetable[m - 1] - 1 # 1분 앞선 시간
            hour, minute = last // 60, last % 60
            return '%02d:%02d' % (hour, minute)
        # 모든 조건에 만족하지 않는 경우
        print(timetable)
        for j in range(m - 1, -1, -1):
            bus_arrive = (60 * 9) + i * t #현재 버스 도착 시간
            if timetable[j] <= bus_arrive: # 앞 선 크루들
                del timetable[j]
n, t, m = 10,60,5
timetable =    ["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]
print(solution(n, t, m, timetable))

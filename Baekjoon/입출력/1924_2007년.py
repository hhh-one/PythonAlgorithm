#리스트 이용
day = 0 # month->day로 합산한 전체일수
day_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week_list = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

m, d = map(int, input().split())

for i in range(m - 1):
    day += day_list[i]

day = (day + d) % 7

print(week_list[day])
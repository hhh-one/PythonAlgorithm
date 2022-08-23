N = int(input())
asc_list = [] #정렬할 리스트 

for i in range(N):
    num = int(input())
    asc_list.append(num)

asc_list.sort() #정렬

for result in asc_list:
    print(result)
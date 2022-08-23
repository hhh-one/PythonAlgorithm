N = int(input())

#첫 시도때는 자릿수 더하는 것을 하나하나 다 했는데 참고해서 map함수를 이용했다
for i in range(N):
    digit = sum(map(int, str(i))) #자릿수 더하기
    result = i + digit
    if result == N:
        print(i)
        break
    
else:
    print(0)
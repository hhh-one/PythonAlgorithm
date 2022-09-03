def solution(arr):
    answer = []
    for i in range(len(arr)):
        arr.append(10) # 인덱스 에러 막기 위해 맨 마지막에 10 추가
        if arr[i] == arr[i+1]:
            continue
        else:
            answer.append(arr[i])
    return answer
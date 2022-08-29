def solution(clothes):
    answer = 1
    d = {}
    
    for x in clothes:
        # 종류로 개수 추가 + 초기화: 안 입을 경우까지
        d[x[1]] = d.get(x[1], 1) + 1

    nums = [v for v in d.values()]

    for i in nums:
        answer *= i
    return answer - 1 # 모두 안 입는 경우 제외
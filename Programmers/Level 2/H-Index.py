def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    for i, x in enumerate(citations):
        if x > i:
            answer += 1
    return answer
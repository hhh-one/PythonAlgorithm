import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while True:
        min1 = heapq.heappop(scoville)
        if len(scoville) == 0 and min1 < K:
            answer = -1
            break
        if min1 > K:
            break
        min2 = heapq.heappop(scoville)
        new_s = min1 + min2 * 2
        heapq.heappush(scoville, new_s)
        answer += 1
    return answer
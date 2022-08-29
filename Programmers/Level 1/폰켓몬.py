def solution(nums):
    n = len(nums)/2
    d = {}
    
    for x in nums:
        d[x] = d.get(x, 0) + 1
    if len(d.keys()) >= n:
        return n
    else:
        return len(d.keys())

# return min(len(nums)/2, len(set(nums))) 로 간단하게 할 수 있다
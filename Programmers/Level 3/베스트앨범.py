def solution(genres, plays):
    answer = []
    d_plays = {}    # 장르별 각 노래의 재생횟수
    d_sum = {}      # 장르별 전체 재생횟수

    for i, (g, p) in enumerate(zip(genres, plays)):
        d_sum[g] = d_sum.get(g, 0) + p
        if g not in d_plays:
            d_plays[g] = [(i, p)]
        else:
            d_plays[g].append((i, p))

    # 전체 재생횟수가 많은 장르부터
    for k, v in sorted(d_sum.items(), key=lambda x : x[1], reverse=True):
        # 장르별 재생횟수가 많은 노래순으로 2개만 answer에 추가
        for i, p in sorted(d_plays[k], key=lambda x : x[1], reverse=True)[:2]:
            answer.append(i)
    return answer
for tc in range(1, int(input()) + 1):
    N = int(input())
    points = list(map(int, input().split()))
    scores = set([0])
    cnt = 1  # bcuz of 0 point, count start from 1
    # Through use 'cnt', we can skip the process which count the length of 'scores'
    able_score = [False] * (sum(points) + 1)
    for point in points:
        tmp = set()
        for score in scores:
            if not able_score[score + point]:
                able_score[score + point] = 1
                tmp.add(score + point)
                cnt += 1
        scores.update(tmp)
    print('#{} {}'.format(tc, cnt))

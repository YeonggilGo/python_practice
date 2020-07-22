T = int(input())

for tc in range(1, T + 1):
    N, tar = map(int, input().split())

    scores_dict = {}
    for i in range(N):
        info = list(map(int, input().split()))
        scores_dict[i] = info[0] * 0.35 + info[1] * 0.45 + info[2] * 0.2

    item = list(scores_dict.items())
    item.sort(key=lambda x: -x[1])

    grade = {
        0: 'A+', 1: 'A0', 2: 'A-', 3: 'B+', 4: 'B0', 5: 'B-', 6: 'C+', 7: 'C0', 8: 'C-', 9: 'D0'
    }

    ans = item.index((tar - 1, scores_dict[tar - 1]))//(N/10)

    print(f'#{tc} {grade[ans]}')

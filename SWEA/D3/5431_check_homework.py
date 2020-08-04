T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    submitters = list(map(int, input().split()))
    students = [1] * (N+1)
    for sub in submitters:
        students[sub] = 0

    print(f'#{tc}',end = ' ')
    for i in range(1,N+1):
        if students[i]:
            print(i,end = ' ')
    print()
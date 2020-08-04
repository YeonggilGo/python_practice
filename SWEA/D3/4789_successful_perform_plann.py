T = int(input())
for tc in range(1, T + 1):
    ans = 0
    people = list(map(int, input()))
    clapping = 0
    for i in range(len(people)):
        if people[i] and clapping < i:
            ans += i - clapping
            clapping = people[i] + i
        else:
            clapping += people[i]
    print(f'#{tc} {ans}')

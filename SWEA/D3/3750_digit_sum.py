# 매 테스트 케이스마다 print를 하지않고
# 배열에 저장해서 한꺼번에 출력하니까 동작시간이 훨씬 줄어들었다.
# 이유가 뭔지는 아직 모르겠다.

T = int(input())
ans = []
for tc in range(1, T + 1):
    N = input()
    while len(N) > 1:
        N_li = list(map(int, N))
        N = str(sum(N_li))
    ans.append(N)

for tc in range(0, T):
    print(f'#{tc+1} {ans[tc]}')

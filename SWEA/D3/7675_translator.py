T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    marks = '.!?'
    sentences = input().replace('?', ' ?').replace('.', ' .').replace('!', ' !').split()
    ans = []
    cnt = 0
    for word in sentences:
        if word.isalpha() and word == word.capitalize():
            cnt += 1
        if word in marks:
            ans.append(cnt)
            cnt = 0

    print(f'#{tc}', *ans)

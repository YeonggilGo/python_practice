T = int(input())

def dfs(num, n, cnt):
    global ans
    if n == cnt:
        num = int(''.join(list(map(str,num))))
        if  num > ans:
            ans = num
        return
    
    for i in range(len(num)):
        for j in range(i + 1, len(num)):
    
            num[i], num[j] = num[j], num[i]
            dfs(num, n, cnt + 1)
            num[i], num[j] = num[j], num[i]
    
    

for tc in range(1, T + 1):
    num, n = input().split()
    ans = 0
    num = list(num)
    n = int(n)


    dfs(num,n,0)
    print(f'#{tc} {ans}')
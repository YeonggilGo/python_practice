N = int(input())

for i in range(1, N+1):
    tmp = ''
    clap = '369'

    for num in clap:
        if num in str(i):
            tmp += '-' * str(i).count(num)

    if tmp:
        print(tmp, end=' ')
    else:
        print(i, end=' ')

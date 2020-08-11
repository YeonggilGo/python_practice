N = int(input())
result = []
count = 1

while True:
    if len(result) == 10:
        break
    else:
        num = count * N
        numList = list(map(int, str(num)))
        count += 1
        for i in numList:
            if i not in result:
                result.append(i)
            else:
                continue
print(num)
print(result)
line = [0, 0]
new_line = [3, 0]

c = not ((line[0] >= new_line[0]) ^ (line[1] <= new_line[1]))
print(line[0] > new_line[0])
print(line[1] < new_line[1])
print(c)

print()
print(False ^ True)

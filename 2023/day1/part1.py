with open('input.txt') as f:
    lines = list(filter(None, map(str.strip, f)))

ans = 0
for line in lines:
    num = 0
    for i in range(len(line)):
        if line[i].isdigit():
            num += int(line[i]) * 10
            break
    for i in range(len(line) - 1, -1, -1):
        if line[i].isdigit():
            num += int(line[i])
            break
    ans += num

print(ans)
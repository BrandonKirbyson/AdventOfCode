with open('input.txt') as f:
    lines = list(filter(None, map(str.strip, f)))

REAL_DIGITS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

def check_digit(line, i):
     if line[i].isdigit():
         return int(line[i])
     
     for name, value in REAL_DIGITS.items():
        if line[i:i + len(name)] == name:
            return value

ans = 0
for line in lines:
    num = 0
    for i in range(len(line)):
        d = check_digit(line, i)
        if d:
           num += d * 10
           break
    for i in range(len(line) - 1, -1, -1):
        d = check_digit(line, i)
        if d:
           num += d
           break
    ans += num

print(ans)
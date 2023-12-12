with open('input.txt') as f:
    nums = [map(int, filter(None, l.strip().split(":")[1].split(" "))) for l in f.read().split("\n")]
    races = zip(nums[0], nums[1])

ans = 1

for time, rec in races:
    strats = 0
    for i in range(time):
        dist = i * (time - i)
        if dist > rec:
            if dist < rec and strats > 1: break
            strats += 1
    ans *= strats

print(ans)

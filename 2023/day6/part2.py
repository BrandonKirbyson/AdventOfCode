with open('input.txt') as f:
    nums = [int(l.strip().split(":")[1].replace(" ", "")) for l in f.read().split("\n")]
    time = nums[0]
    rec = nums[1]

ans = 0
first = 0
last = 0
for i in range(time):
    if i * (time - i) > rec:
        first = i
        break
for i in range(time, 0, -1):
    if i * (time - i) > rec:
        last = i
        break

ans = last - first + 1

print(ans)

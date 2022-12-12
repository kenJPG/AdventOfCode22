inp = open('inputs/day10.txt', 'r').read()

cycles = []

for op in inp.split('\n'):
	move = op.split(' ')[0]
	cycles.append(0)
	if move == 'addx':
		val = op.split(' ')[1]
		val = int(val)
		cycles.append(val)

ans = 0
cur = 1
check = [i for i in range(20, 221, 40)]
for i, cycle in enumerate(cycles):
	if (i + 1) in check:
		ans += (i + 1) * cur
	cur += cycle

print(ans)
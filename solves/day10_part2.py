inp = open('inputs/day10.txt', 'r').read()

cycles = []

for op in inp.split('\n'):
	move = op.split(' ')[0]
	cycles.append(0)
	if move == 'addx':
		val = op.split(' ')[1]
		val = int(val)
		cycles.append(val)

cur = 1
x_pos = 0
y_pos = 0
screen = [['.' for i in range(40)] for j in range(6)]
for i, cycle in enumerate(cycles):
	y_pos = i // 40
	x_pos = i % 40
	if abs(x_pos - cur) <= 1:
		screen[y_pos][x_pos] = '#'
	cur += cycle

for row in screen:
	print("".join(row))
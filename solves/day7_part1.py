inp = open('inputs/day7.txt', 'r').read()

val = {}

path = ['home']

for line in inp.split('\n'):
	splitted = line.split(' ')
	if splitted[0] == '$':
		if splitted[1] == 'cd':
			if splitted[2] == '/':
				path = ['home']
			elif splitted[2] == '..':
				path.pop()
			else:
				path.append(splitted[2])
	else:
		if splitted[0] != 'dir':
			for i in range(len(path)):
				val[",".join(path[:i + 1])] = (val.get(",".join(path[:i + 1])) or 0) + int(splitted[0])

ans = 0
for t in val.values():
	if t <= 100000:
		ans += t

print(ans)

inp = open('inputs/day8.txt', 'r').read().split('\n')

visible = [[0 for i in range(len(inp[0]))] for j in range(len(inp))]

for i, row in enumerate(inp):
	prev = -1
	for j in range(len(row)):
		if int(row[j]) > prev:
			visible[i][j] = 1
			prev = int(row[j])

	prev = -1
	for j in range(len(row) - 1, -1, -1):
		if int(row[j]) > prev:
			visible[i][j] = 1
			prev = int(row[j])

for i in range(len(inp[0])):
	prev = -1
	for j in range(len(inp)):
		if int(inp[j][i]) > prev:
			visible[j][i] = 1
			prev = int(inp[j][i])

	prev = -1
	for j in range(len(inp) - 1, -1, -1):
		if int(inp[j][i]) > prev:
			visible[j][i] = 1
			prev = int(inp[j][i])

ans = 0
for row in visible:
	ans += sum(row)


print(ans)
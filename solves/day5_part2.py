inp = open('inputs/day5.txt', 'r').read().split('\n')

ROW = 8
COLUMN = 9

stacks = []
for i in range(COLUMN):
	stacks.append([])


for i in range(ROW, -1, -1):
	for j in range(COLUMN):
		newchar = inp[i][1 + j * 4]
		if newchar.isalpha():
			stacks[j].append(inp[i][1 + j * 4])


for i in range(ROW + 2, int(len(inp))):
	row = inp[i].split(' ')
	amount = int(row[1])
	u = int(row[3]) - 1
	v = int(row[5]) - 1
	amount = min(amount, len(stacks[u]))
	stacks[v] += stacks[u][-amount:]
	stacks[u] = stacks[u][:-amount]

for i in range(COLUMN):
	print(stacks[i][-1], end="")
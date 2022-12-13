inp = open('inputs/day12.txt', 'r').read().split('\n')

vis = [[0 for _ in range(len(inp[0]))] for i in range(len(inp))]
g = [[0 for _ in range(len(inp[0]))] for i in range(len(inp))]
start = []
end = []
for i, row in enumerate(inp):
	for j, char in enumerate(row):
		if char == 'S':
			g[i][j] = 0
			start = [i, j]
		elif char == 'E':
			g[i][j] = 25
			end = [i, j]
		else:
			g[i][j] = ord(char) - ord('a')

q = []
steps = []
cur = 0
q.append(end)
steps.append(0)
ans = 1e9
while (cur < len(q)):
	if g[q[cur][0]][q[cur][1]] == 0:
		ans = min(ans, steps[cur])
	else:
		dirs = [[0,1], [1,0], [-1,0], [0,-1]]
		for d in dirs:
			i = q[cur][0] + d[0]
			j = q[cur][1] + d[1]
			if i >= 0 and j >= 0 and i < len(inp) and j < len(inp[0]):
				if (g[i][j] - g[q[cur][0]][q[cur][1]]) >= -1 and not vis[i][j]:
					vis[i][j] = 1
					q.append([i, j])
					steps.append(steps[cur] + 1)
	cur += 1
print(ans)
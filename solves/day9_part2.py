inp = open('inputs/day9.txt', 'r').read()

visited = {}

rope_pos = [[0, 0] for i in range(10)]
moves = {
	'U': [0, 1],
	'D': [0, -1],
	'L': [-1, 0],
	'R': [1, 0]
}
visited[",".join(map(str, rope_pos[0]))] = 1
for row in inp.split("\n"):
	move, q = row.split(' ')
	q = int(q)
	for i in range(q):
		rope_pos[0][0] += moves[move][0]
		rope_pos[0][1] += moves[move][1]
		for idx in range(1, 10):
			if max(abs(rope_pos[idx - 1][0] - rope_pos[idx][0]), abs(rope_pos[idx - 1][1] - rope_pos[idx][1])) > 1:
				i_diff = rope_pos[idx - 1][0] - rope_pos[idx][0]
				j_diff = rope_pos[idx - 1][1] - rope_pos[idx][1]
				i_diff = i_diff // (abs(i_diff) or 1)
				j_diff = j_diff // (abs(j_diff) or 1)
				rope_pos[idx][0] += i_diff
				rope_pos[idx][1] += j_diff
			
		visited[",".join(map(str, rope_pos[9]))] = 1

print(sum(visited.values()))
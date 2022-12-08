inp = open('inputs/day8.txt', 'r').read().split('\n')

def out(i, j):
	if i < 0 or j < 0:
		return True
	if i >= len(inp) or j >= len(inp[0]):
		return True
	return False

best_score = 0
for i in range(1, len(inp) - 1):
	for j in range(1, len(inp[0]) - 1):
		dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
		score = 1
		for d in dirs:
			i_d = d[0]
			j_d = d[1]
			cur_i = i
			cur_j = j
			try:
				while True:
					cur_i += i_d
					cur_j += j_d
					if cur_i < 0 or cur_j < 0:
						break
					if (int(inp[cur_i][cur_j]) >= int(inp[i][j]) or out(cur_i + i_d, cur_j + j_d)):
						score *= abs(cur_i - i) + abs(cur_j - j)
						break
			except:
				pass

		# if score > best_score:
		# 	print(i, j)
		best_score = max(score, best_score)


print(best_score)
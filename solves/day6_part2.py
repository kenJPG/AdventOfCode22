inp = open('inputs/day6.txt', 'r').read()

DISTANCE = 14

count = [0] * 26
duplicates = 0

for i in range(0, DISTANCE - 1):
	pos = ord(inp[i]) - ord('a')
	if count[pos] > 0:
		duplicates += 1
	count[pos] += 1

for i in range(DISTANCE - 1, len(inp)):
	if i - DISTANCE >= 0:
		old_pos = ord(inp[i - DISTANCE]) - ord('a')
		if count[old_pos] > 1:
			duplicates -= 1
		count[old_pos] -= 1

	pos = ord(inp[i]) - ord('a')
	if count[pos] > 0:
		duplicates += 1
	count[pos] += 1

	if duplicates == 0:
		print(i + 1)
		break
def priority(val):
	if ord(val) < ord('a'):
		return ord(val) - ord('A') + 27
	return ord(val) - ord('a') + 1


rucksacks = open('inputs/day3.txt', 'r').read().split('\n')

track = [0] * 60

current = 1
ans = 0
for rucksack in rucksacks:
	half = len(rucksack) // 2
	for char in rucksack[:half]:
		track[ord(char) - ord('A')] = current

	for char in rucksack[half:]:
		if track[ord(char) - ord('A')] == current:
			ans += priority(char)
			break
			
	current += 1

print(ans)
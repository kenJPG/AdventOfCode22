def priority(val):
	if ord(val) < ord('a'):
		return ord(val) - ord('A') + 27
	return ord(val) - ord('a') + 1


rucksacks = open('inputs/day3.txt', 'r').read().split('\n')

track = [0] * 60

ans = 0
for idx in range(0, len(rucksacks), 3):
	myset = set(rucksacks[idx])
	for elf_idx in range(3):
		myset = myset.intersection(set(rucksacks[idx + elf_idx]))

	ans += priority([*myset][0])

print(ans)
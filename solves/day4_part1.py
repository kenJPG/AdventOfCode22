inp = open('inputs/day4.txt', 'r').read().split('\n')

ans = 0
for pair in inp:
	first, second = pair.split(',')

	first = list(map(int, first.split('-')))
	second = list(map(int, second.split('-')))

	if (
		(first[0] >= second[0] and first[1] <= second[1])
			or
		(second[0] >= first[0] and second[1] <= first[1])
	):
		ans += 1

print(ans)
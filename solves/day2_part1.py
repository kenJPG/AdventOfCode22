inp = open('inputs/day2.txt', 'r').read()

elf_moves = ['A', 'B', 'C']
my_moves = ['X', 'Y', 'Z']

def gain(elf, me):
	# If my index is 1 greater than (+1) elf's, I win.
	# If my index is same as elf's, it's a tie.
	# if my index is 1 less than (-1) than elf's, I lose.
	elf_idx = elf_moves.index(elf)
	my_idx = my_moves.index(me)

	points = (my_idx - elf_idx + 3) % 3
	# points = 2 if lose (2 is -1 in MOD 3)
	# points = 1 if win
	# points = 0 if draw

	points = (points + 1) % 3 
	# converts to: 
	# > points = 0 if lose
	# > points = 2 if win
	# > points = 1 if draw

	return points * 3 + my_idx + 1

print(sum(list(map(lambda x: gain(*x.split(' ')), inp.split('\n')))))
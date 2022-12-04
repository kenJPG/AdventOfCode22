inp = open('inputs/day2.txt', 'r').read()

elf_moves = ['A', 'B', 'C']
outcome = ['X', 'Y', 'Z']

def gain(elf, me):
	elf_idx = elf_moves.index(elf)
	outcome_idx = outcome.index(me)

	points = outcome_idx * 3 # Outcome points

	# To win, we play the move 1 greater than the elf move
	# To draw, we play the same move as the elf
	# To lose, we play the move 1 less than the elf
	points += ((elf_idx + (outcome_idx - 1)) % 3) + 1
	return points

print(sum(list(map(lambda x: gain(*x.split(' ')), inp.split('\n')))))
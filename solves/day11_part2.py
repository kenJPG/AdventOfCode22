inp = open('inputs/day11.txt', 'r').read().split('\n\n')

monkeys = []
for monkey_inp in inp:
	monkey_id = int(monkey_inp.split('\n')[0].lstrip('Monkey ').rstrip(':'))
	items = monkey_inp.split('\n')[1].lstrip('Starting items:').lstrip().split(', ')
	op = monkey_inp.split('\n')[2].lstrip().lstrip('Operation:').lstrip().lstrip('new =')
	div = monkey_inp.split('\n')[3].split()[-1]
	yes = monkey_inp.split('\n')[4].split()[-1]
	no = monkey_inp.split('\n')[5].split()[-1]
	monkeys.append({
		'items': items,
		'op': op,
		'div': int(div),
		'yes': yes,
		'no': no
	})

# This function computes GCD 
def compute_gcd(x, y):

   while(y):
       x, y = y, x % y
   return x

# This function computes LCM
def compute_lcm(x, y):
   lcm = (x*y)//compute_gcd(x,y)
   return lcm

LCM = 1
for item in list(map(lambda x: x['div'], monkeys)):
	LCM = compute_lcm(LCM, item)

counts = [0 for i in range(len(monkeys))]
for i in range(10000):
	print('i:', i)
	for j in range(len(monkeys)):
		for k in range(len(monkeys[j]['items'])):
			counts[j] += 1
			new = 0
			old = int(monkeys[j]['items'][k])
			new = eval(monkeys[j]['op']) % LCM
			if new % monkeys[j]['div'] == 0:
				monkeys[int(monkeys[j]['yes'])]['items'].append(new)
			else:
				monkeys[int(monkeys[j]['no'])]['items'].append(new)
		monkeys[j]['items'] = []

print(sorted(counts)[-2] * sorted(counts)[-1])
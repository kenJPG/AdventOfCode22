def compare(a, b, show=False):
	if show:
		print(a, b)
	if (type(a) == int) and (type(b) == int):
		if a == b:
			return None
		else:
			return a < b
	elif (type(a) == int):
		return compare([a], b, show)
	elif (type(b) == int):
		return compare(a, [b], show)
	else:
		for i in range(min(len(a), len(b))):
			res = compare(a[i], b[i], show)
			if res == None:
				continue
			else:
				return res
		if len(a) == len(b):
			return None
		else:
			return len(a) < len(b)

inp = open('inputs/day13.txt', 'r').read().split('\n\n')

ans = 0
for i, pair in enumerate(inp):
	a, b = pair.split('\n')
	a = eval(f'list({a})')
	b = eval(f'list({b})')
	if compare(a, b):
		# print(i + 1)
		ans += (i + 1)

print(ans)
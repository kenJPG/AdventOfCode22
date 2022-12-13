import functools

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

def wrap(a, b):
	return -1 if compare(a, b) else 1

inp = open('inputs/day13.txt', 'r').read().split('\n')
inp = (list(filter(lambda x: len(x) != 0, inp)))

mylist = list(map(lambda x: eval(f'list({x})'), inp))
mylist.append([[2]])
mylist.append([[6]])

mylist.sort(key = functools.cmp_to_key(wrap))
print((mylist.index([[2]]) + 1) * (mylist.index([[6]]) + 1))
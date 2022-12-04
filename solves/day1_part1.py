inp = open('inputs/day1.txt', 'r').read()
print(max(map(lambda x: sum(map(int, x.split('\n'))), inp.split('\n\n'))))
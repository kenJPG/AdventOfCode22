inp = open('inputs/day1.txt', 'r').read()
print(sum(sorted(map(lambda x: sum(map(int, x.split('\n'))), inp.split('\n\n')))[-3:]))
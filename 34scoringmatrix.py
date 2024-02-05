# 34scoringmatrix.py by Clarissa Kung
# Worked together in student Coderie

nts = 'ACGT'

print('  ', end=' ') # space at beginning of header
for nt in nts:
	print(nt, end='  ')
print()

for nt1 in nts:
	print(nt1, end=' ')
	for nt2 in nts:
		if nt1 == nt2: print('+1', end=' ')
		else:			print('-1', end=' ')
	print()
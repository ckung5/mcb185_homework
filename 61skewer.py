# 61skewer.py by Clarissa Kung

import dogma
import sys
import mcb185

'''
seq = 'ACGTACGTGGGGGACGTACGTCCCCC'
w = 10
for i in range(len(seq) -w + 1):
	s = seq[i:i+w]
	print(i, dogma.gc_comp(s), dogma.gc_skew(s))
'''

path = sys.argv[1]
w = int(sys.argv[2])

for defline, seq in mcb185.read_fasta(path):
	for i in range(len(seq) - w + 1):
		win = seq[i:i+w]
		print(i, dogma.gc_comp(win), dogma.gc_skew(win))
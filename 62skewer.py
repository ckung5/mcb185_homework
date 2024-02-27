# 62skewer.py by Clarissa Kung

import dogma
import sys
import mcb185

path = sys.argv[1]
windowsize = int(sys.argv[2])

for defline, seq in mcb185.read_fasta(path):
	
	# Initial window
	window = seq[:windowsize]
	initial_gccomp = dogma.gc_comp(window)
	initial_gcskew = dogma.gc_skew(window)
	print(0, initial_gccomp, initial_gcskew)

	c_count = window.count('C')
	g_count = window.count('G')
	
	for i in range(len(seq) - windowsize + 1):
		left_nt = seq[i]
		right_nt = seq[i + windowsize - 1]
		
		if left_nt == 'C':
			c_count -= 1
		elif left_nt == 'G':
			g_count -= 1
		
		if right_nt == 'C':
			c_count += 1
		elif right_nt == 'G':
			g_count += 1
		
		# Calculation for current gc_comp
		new_gccomp = (c_count + g_count) / windowsize
		
		# Calculation for current gc_skew
		# Accounted for dividing by 0 error
		if c_count == g_count:
			new_gcskew = 0
		else: 
			new_gcskew = (g_count - c_count) / (g_count + c_count)
			
		print(i, new_gccomp, new_gcskew)
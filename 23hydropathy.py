# 23hydropathy.py by Clarissa Kung

import sys

def hydropathy(aa):
	if aa == 'A': return 1.80
	elif aa == 'C': return 2.50
	elif aa == 'D': return -3.50
	elif aa == 'E': return -3.50
	elif aa == 'F': return 2.80
	elif aa == 'G': return -0.40
	elif aa == 'H': return -3.20
	elif aa == 'I': return 4.50
	elif aa == 'K': return -3.90
	elif aa == 'L': return 3.80
	elif aa == 'M': return 1.90
	elif aa == 'N': return -3.50
	elif aa == 'P': return -1.60
	elif aa == 'Q': return -3.50
	elif aa == 'R': return -4.50
	elif aa == 'S': return -0.80
	elif aa == 'T': return -0.70
	elif aa == 'V': return 4.20
	elif aa == 'W': return -0.90
	elif aa == 'Y': return -1.30
	else: 			sys.exit('Error: Not a valid amino acid letter')
	
	
print(hydropathy('A'))
print(hydropathy('S'))
print(hydropathy('M'))
print(hydropathy('B'))

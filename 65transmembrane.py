# 65transmembrane.py by Clarissa Kung

import dogma
import mcb185
import sys

def has_proline(seq):
	if 'P' in seq:
		return True
	return False
	
def has_region(region, winsize, kd_threshold):
	for i in range(len(region) - winsize + 1):
		win = region[i:i+winsize]
		
		sum_kd = 0
		for aa in win:
			sum_kd += dogma.hydropathy(aa)
		avg_kd = sum_kd / winsize
		
		if avg_kd >= kd_threshold and not has_proline(win):
			return True
	return False

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	signal_peptide = seq[:30]
	transmembrane_region = seq[30:]
	if (has_region(signal_peptide, 8, 2.5) and 
		has_region(transmembrane_region, 11, 2.0)):
		print(defline[0:60])
# 65transmembrane.py by Clarissa Kung

import dogma
import mcb185
import sys

def has_proline(seq):
	if 'P' in seq:
		return True
	return False
	
def has_signal_peptide(signal_peptide):
	sp_winsize = 8
	for i in range(len(signal_peptide) - sp_winsize + 1):
		sp_win = signal_peptide[i:i+sp_winsize]
		
		# calculate sum and average of KD values of signal peptides
		sum_spkd = 0
		for aa in sp_win:
			sum_spkd += dogma.hydropathy(aa)
		avg_spkd = sum_spkd / sp_winsize
		
		if avg_spkd >= 2.5 and not has_proline(sp_win):
			return True
	return False
	
def has_transmembrane_protein(transmembrane_region):
	tmr_winsize = 11
	for i in range(len(transmembrane_region) - tmr_winsize + 1):
		tmr_win = transmembrane_region[i:i+tmr_winsize]
		
		# calculate sum and average of KD values of transmembrane regions
		sum_tmrkd = 0
		for aa in tmr_win:
			sum_tmrkd += dogma.hydropathy(aa)
		avg_tmrkd = sum_tmrkd / tmr_winsize
		
		if avg_tmrkd >= 2.0 and not has_proline(tmr_win):
			return True
	return False
	
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	signal_peptide = seq[:30]
	transmembrane_region = seq[30:]
	if (has_signal_peptide(signal_peptide) and 
		has_transmembrane_protein(transmembrane_region)):
		print(defline[0:60])
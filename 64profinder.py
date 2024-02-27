# 64profinder.py by Clarissa Kung

import dogma
import sys
import mcb185

path = sys.argv[1]
min_aas = int(sys.argv[2])

def six_frame_translation(dna):
	frames = []
	
	# Forward frames
	for i in range(3):
		frames.append(dogma.translate(dna[i:]))
	
	# Reverse frames
	rev_dna = dogma.revcomp(dna)
	for i in range(3):
		frames.append(dogma.translate(rev_dna[i:]))
			
	return frames

def gene_finder(seq, min_aas):
	proteins = []
	translated_seq = six_frame_translation(seq)
	
	for fr in translated_seq:
		# initialize variables to determine protein start
		protein_start = False
		protein_seq = ''
		for aa in fr:
			if aa == 'M':
				protein_start = True
			if protein_start:
				if aa == '*':
					if len(protein_seq) >= min_aas:
						proteins.append(protein_seq)
					protein_seq = ''
					protein_start = False
				else:
					protein_seq += aa
	return proteins
	
for defline, seq in mcb185.read_fasta(path):
	final_seq = gene_finder(seq, min_aas)
	print(len(final_seq))
	protein_count = 0
	
	for protein in final_seq:
		print(f'{defline[0:11]}-prot-{protein_count}')
		print(protein)
		protein_count += 1
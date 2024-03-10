# 64profinder.py by Clarissa Kung

import dogma
import sys
import mcb185

path = sys.argv[1]
min_aas = int(sys.argv[2])

def six_frame_translation(dna):
	frames = []
	rev_dna = dogma.revcomp(dna)
	
	for i in range(3):
		# Forward frames
		frames.append(dogma.translate(dna[i:]))
		# Reverse frames
		frames.append(dogma.translate(rev_dna[i:]))		
	return frames

def gene_finder(seq, min_aas):
	proteins = []
	translated_seq = six_frame_translation(seq)
	
	for frame in translated_seq:
		for aas in frame.split('*'):
			m_index = aas.find('M')
			if m_index != -1 and len(aas[m_index:]) >= min_aas:
					proteins.append(aas)
			
	return proteins
	
for defline, seq in mcb185.read_fasta(path):
	final_seq = gene_finder(seq, min_aas)
	protein_count = 0
	
	for protein in final_seq:
		print(f'{defline[0:11]}-prot-{protein_count}')
		print(protein)
		protein_count += 1
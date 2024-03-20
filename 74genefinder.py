# 74genefinder.py by Clarissa Kung 

import mcb185
import dogma
import sys

path = sys.argv[1]
min_orf_len = int(sys.argv[2])

def six_frame_translation(dna):
	frames = []
	rev_dna = dogma.revcomp(dna)
	
	for i in range(3):
		# Forward frames
		frames.append(dogma.translate(dna[i:]))
		# Reverse frames
		frames.append(dogma.translate(rev_dna[i:]))		
	return frames

# Function to convert amino acids indices to nucleotide indices
def aas_to_nts(aas, frame, strand, seq):
	nts = []
	for i in aas:
		if strand == '+':
			nt_start = frame * 3 + i * 3
			nt_end = nt_start + min_orf_len * 3
			nts.append((nt_start, nt_end))
		else:
			nt_end = len(seq) - (frame * 3 + i * 3)
			nt_start = nt_end - min_orf_len * 3
			nts.append((nt_start, nt_end))
	return nts
	
def gene_finder(seq, min_orf_len):
	genes = {}
	proteins = []
	
	translated_seq = six_frame_translation(seq)
	
	for frame in range(3):
		for strand in ['+', '-']:
			if strand == '+':
				seq_index = frame
			else:
				seq_index = frame + 3
				
			for i, aas in enumerate(translated_seq[seq_index].split('*')):
				m_index = aas.find('M')
				if m_index != -1 and len(aas[m_index:]) >= min_orf_len:
					nts = aas_to_nts([m_index], frame, strand, seq)
					gene_num = f'gene{len(genes) + 1}'
					genes[gene_num] = nts[0] + (strand,)
					proteins.append(aas)
					
	return genes, proteins
	
def print_gff(gene_coords, gene_num):
	gff_lines = []
	for gene_type, gene_info in zip(gene_coords.keys(), gene_coords.values()):
		start, end, strand = gene_info
		attributes = f'ID={gene_num}'
		gff_lines.append(f'E.coli\tputative_gene\tCDS\t{start}\t{end}\t.\t{strand}\t.\t{attributes}')
	return '\n'.join(gff_lines)

ecoli_genome = ''
for defline, seq in mcb185.read_fasta(path):
	ecoli_genome += seq
	
gene_coord, defline = gene_finder(ecoli_genome, min_orf_len)
gff_content = print_gff(gene_coord, gene_num='gene')

print(gff_content)
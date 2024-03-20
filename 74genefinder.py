# 74genefinder.py by Clarissa Kung 

import mcb185
import dogma
import sys

# Function used to perform six-frame translation of DNA sequence
def six_frame_translation(dna):
	frames = []
	rev_dna = dogma.revcomp(dna)
	
	for i in range(3):
		# Forward frames
		frames.append(dogma.translate(dna[i:]))
		# Reverse frames
		frames.append(dogma.translate(rev_dna[i:]))		
	return frames
	
# Function used to find genes within the DNA sequence based on requirements and
# determines the specific coordinates of those genes
def gene_finder(seq, min_orf_len):
	genes = {} # Dictionary to store gene coordinates
	proteins = [] # List to store translated proteins
	translated_seq = six_frame_translation(seq)
	
	for frame in range(3):
		for strand in ['+', '-']:
			if strand == '+':
				seq_index = frame
			else:
				seq_index = frame + 3
				
			# Split translated sequence into individual amino acid sequences
			# using stop codon
			for i, aas in enumerate(translated_seq[seq_index].split('*')):
				m_index = aas.find('M')
				if m_index != -1 and len(aas[m_index:]) >= min_orf_len:
					nt_start = frame * 3 + m_index * 3
					nt_end = nt_start + min_orf_len * 3
					if strand == '-':
						nt_end = len(seq) - nt_start
						nt_start = nt_end - min_orf_len * 3
					gene_num = f'gene{len(genes) + 1}'
					genes[gene_num] = (nt_start, nt_end, strand)
					proteins.append(aas)
					
	return genes, proteins
	
def generate_gff(gene_coords, gene_num):
	gff_lines = []
	for gene_type, gene_info in gene_coords.items():
		start, end, strand = gene_info
		gff_lines.append(
			f'E.coli\tputative_gene\tCDS\t{start}\t{end}\t.\t'
			f'{strand}\t.\tID={gene_num}')
	return '\n'.join(gff_lines)

path = sys.argv[1]
min_orf_len = int(sys.argv[2])

for defline, seq in mcb185.read_fasta(path):
	ecoli_genome = ''.join(seq)
	gene_coord, defline = gene_finder(ecoli_genome, min_orf_len)
	gff_content = generate_gff(gene_coord, f'gene')
	
print(gff_content)
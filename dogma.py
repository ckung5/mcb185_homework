# dogma.py by Clarissa Kung

import math

def transcribe(dna):
	return dna.replace('T', 'U')
	
def revcomp(dna):
	rc = []
	for nt in dna[::-1]:
		if nt == 'A': rc.append('T')
		elif nt == 'C': rc.append('G')
		elif nt == 'G': rc.append('C')
		elif nt == 'T': rc.append('A')
		else:			rc.append('N')
	return ''.join(rc)
	
def translate(dna):
	aas = []
	for i in range(0, len(dna), 3):
		codon = dna[i:i+3]
		if codon == 'ATG': 
			aas.append('M')
		elif codon == 'ATA' or codon == 'ATC' or codon == 'ATT': 
			aas.append('I')
		elif codon == 'ACA' or codon == 'ACC' or codon == 'ACG' or codon == 'ACT':
			aas.append('T')
		elif codon == 'AAC' or codon == 'AAT':
			aas.append('N')
		elif codon == 'AAA' or codon == 'AAG':
			aas.append('K')
		elif codon == 'AGC' or codon == 'AGT':
			aas.append('S')
		elif codon == 'AGA' or codon == 'AGG':
			aas.append('R')
		elif codon == 'CTA' or codon == 'CTC' or codon == 'CTG' or codon == 'CTT':
			aas.append('L')
		elif codon == 'CCA' or codon == 'CCC' or codon == 'CCG' or codon == 'CCT':
			aas.append('P')
		elif codon == 'CAC' or codon == 'CAT':
			aas.append('H')
		elif codon == 'CAA' or codon == 'CAG':
			aas.append('Q')
		elif codon == 'CGA' or codon == 'CGC' or codon == 'CGG' or codon == 'CGT':
			aas.append('R')
		elif codon == 'GTA' or codon == 'GTC' or codon == 'GTG' or codon == 'GTT':
			aas.append('V')
		elif codon == 'GCA' or codon == 'GCC' or codon == 'GCG' or codon == 'GCT':
			aas.append('A')
		elif codon == 'GAC' or codon == 'GAT':
			aas.append('D')
		elif codon == 'GAA' or codon == 'GAG':
			aas.append('E')
		elif codon == 'GGA' or codon == 'GGC' or codon == 'GGG' or codon == 'GGT':
			aas.append('G')
		elif codon == 'TCA' or codon == 'TCC' or codon == 'TCG' or codon == 'TCT':
			aas.append('S')
		elif codon == 'TTC' or codon == 'TTT':
			aas.append('F')
		elif codon == 'TTA' or codon == 'TTG':
			aas.append('L')
		elif codon == 'TAC' or codon == 'TAT':
			aas.append('Y')
		elif codon == 'TGC' or codon == 'TGT':
			aas.append('C')
		elif codon == 'TGG':
			aas.append('W')
		elif codon == 'TAA' or codon == 'TAG' or codon == 'TGA': 
			aas.append('*')
		else:
			aas.append('X')
	return ''.join(aas)
	
def gc_comp(seq):
	return (seq.count('C') + seq.count('G')) / len(seq)
	
def gc_skew(seq):
	c = seq.count('C')
	g = seq.count('G')
	if c + g == 0: return 0
	return (g - c) / (g + c)
	
def shannon_entropy(a, t, c, g):
	nt_tot = a + t + c + g
	
	if a != 0:
		a_exp = (a / nt_tot) * math.log2(a / nt_tot)
	else:
		a_exp = 0
		
	if t != 0:
		t_exp = (t / nt_tot) * math.log2(t / nt_tot)
	else:
		t_exp = 0
		
	if g != 0:
		g_exp = (g / nt_tot) * math.log2(g / nt_tot)
	else:
		g_exp = 0
		
	if c != 0:
		c_exp = (c / nt_tot) * math.log2(c / nt_tot)
	else:
		c_exp = 0
	
	entropy = -(a_exp + c_exp + g_exp + c_exp)
	return entropy

# from 23hydropathy.py
def hydropathy(aa):
	if aa == 'A': kd = 1.80
	elif aa == 'C': kd = 2.50
	elif aa == 'D': kd = -3.50
	elif aa == 'E': kd = -3.50
	elif aa == 'F': kd = 2.80
	elif aa == 'G': kd = -0.40
	elif aa == 'H': kd = -3.20
	elif aa == 'I': kd = 4.50
	elif aa == 'K': kd = -3.90
	elif aa == 'L': kd = 3.80
	elif aa == 'M': kd = 1.90
	elif aa == 'N': kd = -3.50
	elif aa == 'P': kd = -1.60
	elif aa == 'Q': kd = -3.50
	elif aa == 'R': kd = -4.50
	elif aa == 'S': kd = -0.80
	elif aa == 'T': kd = -0.70
	elif aa == 'V': kd = 4.20
	elif aa == 'W': kd = -0.90
	elif aa == 'Y': kd = -1.30
	return kd

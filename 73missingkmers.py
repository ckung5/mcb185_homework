# 73missingkmers.py by Clarissa Kung

import itertools
import mcb185
import sys
import dogma

k = 1
missing_kmers = False

while not missing_kmers:
	kcount = {}
	for defline, seq in mcb185.read_fasta(sys.argv[1]):
		for i in range(len(seq) - k + 1):
			kmer = seq[i:i+k]
			rev_kmer = dogma.revcomp(kmer)
			if kmer not in kcount: 
				kcount[kmer] = 0
			kcount[kmer] += 1
			if rev_kmer not in kcount:
				kcount[rev_kmer] = 0
			kcount[rev_kmer] += 1
	
	for nts in itertools.product('ACGT', repeat=k):
		current_kmer = ''.join(nts)
		if current_kmer not in kcount:
			missing_kmers = True
			print(current_kmer)
			
	k += 1
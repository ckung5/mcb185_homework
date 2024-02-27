# 63dust.py by Clarissa Kung

import dogma
import sys
import mcb185

path = sys.argv[1]
window_size = int(sys.argv[2])
ent_threshold = float(sys.argv[3])

for defline, seq in mcb185.read_fasta(path):
	masked_seq = ''

	# For loop to loop through each window
	for i in range(0, len(seq) - window_size + 1, window_size):
		win = seq[i:i+window_size]
		
		a_count = win.count('A')
		t_count = win.count('T')
		c_count = win.count('C')
		g_count = win.count('G')
		entropy = dogma.shannon_entropy(a_count, t_count, c_count, g_count)
	
		if entropy < ent_threshold:
			masked_seq += 'N' * window_size
		else:
			masked_seq += win

# Print with lines wrapped at 60 characters
print(f'>{defline}', end='\n')
for i in range(0, len(masked_seq), 60):
	print(masked_seq[i:i+60])
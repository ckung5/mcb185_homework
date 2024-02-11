# 43randomdna.py by Clarissa Kung

import random

seq = 0
for i in range(3):
	seq += 1
	print(f'>seq-{seq}')
	len = random.randint(50, 60)
	for i in range(len):
		nts = random.choice('ACGT')
		print(nts, end='')
	print()
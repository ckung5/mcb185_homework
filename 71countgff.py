# 71countgff.py by Clarissa Kung

import gzip
import sys

count = {}
with gzip.open(sys.argv[1], 'rt') as fp:
	for line in fp:
		if line.startswith('#'): continue
		f = line.split()
		feature = f[2]
		if feature not in count: count[feature] = 0
		count[feature] += 1
# for f, n in count.items(): print(f, n)

# for nt in count:
# 	if nt not in count: count[nt] = 0
# 	count[nt] += 1
	
# for k in sorted(count): print(k, count[k])

for k, v in sorted(count.items(), key=lambda item: item[0]):
	print(k, v)
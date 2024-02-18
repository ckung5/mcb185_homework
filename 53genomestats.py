# 53genomestats.py by Clarissa Kung

import gzip
import sys

gffpath = sys.argv[1]
feature = sys.argv[2]

vals = []
with gzip.open(gffpath, 'rt') as fp:
	for line in fp:
		words = line.split()
		if words[2] == feature:
			beg = int(words[3])
			end = int(words[4])
			vals.append(end - beg + 1)
	
# Count
num = len(vals)
print(f'count: {num}')

# Minimum
mini = vals[0]
for length in vals: 
	if length < mini: mini = length
print(f'minimum: {mini}')
	
# Maximum
maxi = vals[0]
for length in vals:
	if length > maxi: maxi = length
print(f'maximum: {maxi}')
	
# Mean
total = 0
for length in vals:
	total += length
mean = total / num
print(f'mean: {mean:.0f}')

# Standard Deviation
sum_squares = 0
for length in vals:
	sum_squares += (length - mean) ** 2
std_dev = (sum_squares / num) ** 0.5
print(f'standard deviation: {std_dev:.0f}')

# Median
vals.sort()
if len(vals) % 2 == 0:
	median = (vals[len(vals)//2] + vals[(len(vals)//2) - 1]) / 2
else:
	median = vals[len(vals) // 2]
print(f'median: {median:.0f}')


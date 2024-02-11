# 45dndstats.py by Clarissa Kung

import random

# 3D6: roll 3 six-sided dice
rolls = 10000
total = 0

for i in range(rolls):
	for j in range(3):
		d1 = random.randint(1, 6)
		d2 = random.randint(1, 6)
		d3 = random.randint(1, 6)
		stat = d1 + d2 + d3
	total += stat
print(total / rolls)

# 3D6r1: roll 3 six-sided dice, but re-roll any 1s
rolls = 10000
total = 0

for i in range(rolls):
	for j in range(3):
		d1 = random.randint(1, 6)
		d2 = random.randint(1, 6)
		d3 = random.randint(1, 6)
		if d1 == 1: d1 = random.randint(1, 6)
		if d2 == 1: d2 = random.randint(1, 6)
		if d3 == 1: d3 = random.randint(1, 6)
		stat = d1 + d2 + d3
	total += stat
print(total / rolls)

# 3D6x2: roll pairs of six-sided 3 times, taking the maximum each time
rolls = 100000
total = 0

for i in range(rolls):
	stat = 0
	for j in range(3):
		d1 = random.randint(1, 6)
		d2 = random.randint(1, 6)
		if d1 > d2:
			stat += d1
		else:
			stat += d2
	total += stat
print(total / rolls)

# 4D6d1: roll 4 six-sided dice, dropping the lowest die roll
rolls = 100000
total = 0

for i in range(rolls):
	stat = 0
	while True:
		d1 = random.randint(1, 6)
		d2 = random.randint(1, 6)
		d3 = random.randint(1, 6)
		d4 = random.randint(1, 6)
		if d1 <= d2 and d1 <= d3 and d1 <= d4:
			stat = d2 + d3 + d4
			break
		if d2 <= d1 and d2 <= d3 and d2 <= d4:
			stat = d1 + d3 + d4
			break
		if d3 <= d1 and d3 <= d2 and d3 <= d4:
			stat = d1 + d2 + d4
			break
		if d4 <= d1 and d4 <= d2 and d4 <= d3:
			stat = d1 + d2 + d3
			break
	total += stat
print(total / rolls)
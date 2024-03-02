# 57birthday.py by Clarissa Kung

import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

same_bday = 0
for i in range(trials):
	calendar = []
	for j in range(days):
		calendar.append(0)
	for j in range(people):
		bday = random.randint(0, days - 1)
		calendar[bday] += 1
		if calendar[bday] > 1:
			same_bday += 1
			break
			
print(same_bday / trials)
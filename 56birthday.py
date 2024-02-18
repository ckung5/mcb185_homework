# 56birthday.py by Clarissa Kung

import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

same_bday = 0
for i in range(trials):
	birthdays = []
	for j in range(people):
		bday = random.randint(1, days)
		# if loop to check if birthday is in list and 
		# breaks if birthday is in list
		if bday in birthdays:
			same_bday += 1
			break
		birthdays.append(bday)
		
print(same_bday / trials)
# 47deathsaves.py by Clarissa Kung

import random

rolls = 10000
die = 0
stable = 0
revive = 0

for i in range(rolls):
	failures = 0
	successes = 0
	
	while True:
		d = random.randint(1, 20)
		if d == 1:
			failures += 2
		elif d == 20:
			revive += 1
			break
		elif d >= 10:
			successes += 1
		else:
			failures += 1
	
		if failures >= 3:
			die += 1
			break
		elif successes >= 3:
			stable += 1
			break
	
print(die / rolls)
print(stable / rolls)
print(revive / rolls)
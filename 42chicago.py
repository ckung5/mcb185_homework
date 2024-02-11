# 42chicago.py by Clarissa Kung

import random
import sys

"""
zerogames = 0
total_score = 0
games_played = 1000000
for i in range(games_played):
	score = 0
	for roundnumber in range(2, 13):
		d1 = random.randint(1, 6)
		d2 = random.randint(1, 6)
		if d1 + d2 == roundnumber:
			score += roundnumber
	
	total_score += score	
	if score == 0:
		zerogames += 1
		
print(zerogames / games_played)
print(total_score / games_played)
"""

games = 1000000 # 1 million trials
log = games // 100
total = 0
zeroes = 0
for i in range(games):
	if i % log == 0: print(f'{100 * i/games:.0f}', file=sys.stderr)
	score = 0
	for target in range(2, 13):
		# d1 = random.randint(1, 6)
		# d2 = random.randint(1, 6)
		# if d1 + d2 == target
		if random.randint(1, 6) + random.randint(1, 6) == target:
			score += target
	if score == 0: zeroes += 1
	total += score
print(total / games)
print(zeroes / games)


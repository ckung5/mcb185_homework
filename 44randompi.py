# 44randompi.py by Clarissa Kung

import random

in_circle = 0
total = 0

while True:
	x = random.random()
	y = random.random()
	dist = ((x ** 2) + (y ** 2)) ** 0.5
	total += 1
	if dist < 1: in_circle += 1
	pi = 4 * in_circle / total
	print(pi)
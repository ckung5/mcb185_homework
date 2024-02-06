# Author: Christina, Clarissa

pi = 1
pie = 3
for n in range(2, 100, 4):
	mark = (4 / (n * (n + 1) * (n + 2))) - (4 / ((n + 2) * (n + 3) * (n + 4)))
	pie = pie + mark
	print(pie, end=' ')
	
	tab = - (1 / (n + 1)) + (1 / (n + 3))
	pi = pi + tab
	last = pi * 4
	print(last)

"""
pi = 1
pie = 3
for n in range(2, 100, 4):
	mark = (4 / (n * (n + 1) * (n + 2))) - (4 / ((n + 2) * (n + 3) * (n + 4)))
	pie = pie + mark
	print(pie, end=' ')
	
	tab = (1 / (n + 1))
	if (n + 1) % 3 == 1: pi = pi - tab
	if (n + 1) % 3 == 
	last = pi * 4
	print(last)
"""
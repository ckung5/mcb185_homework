# 33triples.py by Clarissa Kung

for a in range(1, 101):
	for b in range(a + 1, 101):
		c = (a**2 + b**2) ** 0.5
		if c % 1 == 0:
			print(a, b, c)

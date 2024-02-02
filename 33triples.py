# 33triples.py by Clarissa Kung

for a in range(1, 101):
	for b in range(a+1, 101):
		for c in range(b+1, 101):
			if a**2 + b**2 == c**2:
				print(a, b, c, sep=',')

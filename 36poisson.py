# 36poisson.py by Clarissa Kung

import math

def poisson_probability(k, n):
	return (n ** k) * math.exp(-n) / math.factorial(k)
	
print(poisson_probability(2, 3))
print(poisson_probability(1, 8))
print(poisson_probability(9, 2))
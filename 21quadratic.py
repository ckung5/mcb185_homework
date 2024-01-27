# 21quadratic.py by Clarissa Kung

import math
import sys

def quadratic(a, b, c):
	discriminant = b**2 - 4*a*c
	
	if discriminant >= 0:
		x1 = (-b + math.sqrt(discriminant)) / (2*a)
		x2 = (-b - math.sqrt(discriminant)) / (2*a)
		return x1, x2
	else: sys.exit('Error: discriminant must be greater than 0')
	
	
print(quadratic(1, -5, 3))
print(quadratic(-2, 8, 4))
print(quadratic(6, 8, -3))
print(quadratic(-5, 6, -2)) # gives a negative discriminant

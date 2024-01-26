# 20demo.py by Clarissa Kung

import math
import sys

print('hello, again') # greeting

print(1.5e-2)
print(1 + 1)
print(2 ** 3)
print(5 % 2)
print(5 * (2+1))
print(pow(2, 3))
print(math.pow(2, 3))
print(math.sqrt(2))
print(math.log(2))
print(0.1 * 1)
print(0.1 * 3)

a = 3                       # side of triangle
b = 4                       # side of triangle
c = math.sqrt(a**2 + b**2)  # hypotenuse
print (c)
print(type(a), type(b), type(c))
print(type(a), type(b), type(c), sep=', ')

def greeting():
    print('hello yourself')
    
def neg_to_pos(x):
	assert(x < 0)
	return abs(x)
	
print(neg_to_pos(-10))

def cube_volume(a):
	assert(a > 0)
	return math.pow(a, 3)
	
print(cube_volume(5))

def cel_to_kelvin(x):
	return (x + 273.15)

print(cel_to_kelvin(50))
print(cel_to_kelvin(-10))

def mph_to_kph(x):
	if x <= 0: sys.exit('error: x must be greater than 0')
	return (x * 1.61)
	
print(mph_to_kph(10))

def calc_dna_conc(od260, df):
	# DNA conc = OD260 * 50 ug/mL * dilution factor
	# df = dilution_factor
	return (od260 * 50 * df)
	
print (calc_dna_conc(0.8, 50))

def calc_dist(x1, x2, y1, y2):
	dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
	return dist
	
print(calc_dist(5, 10, 4, 8))

def midpoint(x1, x2, y1, y2):
	mx = (x1 + x2) / 2
	my = (y1 + y2) / 2
	return mx, my

x, y = midpoint(1, 4, 3, 8)
print(x, y, sep=', ')

a = 2
b = 6
c = a == b
print(c)
print(type(c))

def is_integer(x):
	if x == x // 1: return True
	return False

print(is_integer(5))

def is_odd(num):
	return num % 2 != 0

	if is_odd(num): return True
	else:			return False
		
print(is_odd(7))
		
def is_valid_probability(num):
	return 0 <= num <= 1
	
	if is_valid_probability(p): return True
	else:						return False
		
print(is_valid_probability(1.25))


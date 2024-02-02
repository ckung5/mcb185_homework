# 30demo.py by Clarissa Kung

import math

# while True:
# 	print('hello')
	
i = 0
while True:
	i = i + 1
	print('hey', i)
	if i == 3: break
 	
i = 0
while i < 3:
	print(i)
	i = i + 1
print('final value of i is', i)
 
i = 1
while i < 10:
	print(i)
	i = i + 3
print('final value of i is', i)

for i in range(1, 10, 3):
	print(i)
 	
for i in range(0, 5):
	print(i)
 
for i in range(5):
	print(i)
 	
for char in 'hello':
	print(char)
	
seq = 'GAATTC'
for nt in seq:
 	print(nt)
 	
limit = 4
for i in range(0, limit):
	for j in range(i + 1, limit):
		print(i+1, j+1)
		
limit = 4
for i in range(0, limit):
	for j in range(0, limit):
		print(i+1, j+1)
		
limit = 4
for i in range(0, limit):
	for j in range(i, limit):
		print(i+1, j+1)
		
limit = 4
for i in range(0, limit):
	for j in range(i+1, limit):
		print(i+1, j+1)
		
def triangular(n):
	tri = 0
	for i in range(n+1):
		tri = tri + 1
	return tri
print(triangular(5))

def factorial(n):
	if n == 0: return 1
	fac = 1
	for i in range(1, n + 1):
		fac = fac * i
	return fac
print(factorial(3))

def euler(limit):
	e = 0
	for n in range(limit):
		e = e + 1 / factorial(n)
	return e
print(euler(10))

def is_perfect_square(n):
	root = math.sqrt(n)
	if math.isclose(root, root // 1): return True
	return False
print(is_perfect_square(10))

def is_prime(n):
	for den in range(2, n//2):
		if n % den == 0: return False
	return True
print(is_prime(10))

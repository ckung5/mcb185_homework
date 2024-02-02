# 35nchoosek.py by Clarissa Kung

def factorial(n):
	if n == 0 or n == 1: return 1
	else: 				 return n * (factorial(n - 1))
	
def n_choose_k(n, k):
	if k < 0 or k > n: 
		return 0
	else: 
		return factorial(n) // (factorial(k) * factorial(n - k))
	
print(n_choose_k(5, 2))
print(n_choose_k(9, 4))
print(n_choose_k(1, 10))
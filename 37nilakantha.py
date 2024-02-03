# 37nilakantha.py by Clarissa Kung

def estimate_pi(iterations):
	result = 3.0 
	sign = 1.0 # determines whether term is added or subtracted
	
	for n in range(1, iterations + 1):
		denominator = 2 * n * (2 * n + 1) * (2 * n + 2)
		term = 4 / denominator
		result = result + sign * term
		sign = sign * (-1)
		
	return result
	
print(estimate_pi(3))
print(estimate_pi(45))
print(estimate_pi(100))
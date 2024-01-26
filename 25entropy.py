# 25entropy.py by Clarissa Kung

import math
import sys

def entropy(a, t, c, g):
	nt_total = a + t + c + g
	assert(nt_total > 0)
	
	a_prob = a / nt_total
	t_prob = t / nt_total
	g_prob = g / nt_total
	c_prob = c / nt_total
	
	if a_prob <= 0: sys.exit('Error: The probability of A is less than 0')
	a_exp = a_prob * math.log2(a_prob)
	if t_prob <= 0: sys.exit('Error: The probability of T is less than 0')
	t_exp = t_prob * math.log2(t_prob)
	if g_prob <= 0: sys.exit('Error: The probability of G is less than 0')
	g_exp = g_prob * math.log2(g_prob)
	if c_prob <= 0: sys.exit('Error: The probability of C is less than 0')
	c_exp = c_prob * math.log2(c_prob)
	
	entropy = -(a_exp + c_exp + g_exp + c_exp)
	return entropy
	
	
print(entropy(1, 5, 7, 9))
print(entropy(6, 4, 8, 11))
print(entropy(0, 4, 0, 0)) # should get an error

# 22oligotemp.py by Clarissa Kung

def oligo_temp(a, t, c, g):
	total_nt = a + t + c + g
	
	if total_nt <= 13: tm = (a + t)*2 + (g + c)*4
	else: 	tm = 64.9 + 41 * (g + c - 16.4) / total_nt
	return tm
	
	
print(oligo_temp(5, 3, 7, 9))
print(oligo_temp(9, 7, 8, 11))
print(oligo_temp(2, 4, 1, 5))

# 46savingthrows.py by Clarissa Kung

import random

rolls = 100000
dc_5 = 5
dc_10 = 10
dc_15 = 15

norm_5_successes = 0
norm_10_successes = 0
norm_15_successes = 0
adv_5_successes = 0
adv_10_successes = 0
adv_15_successes = 0
dis_5_successes = 0
dis_10_successes = 0
dis_15_successes = 0

print('DC', 'norm', 'adv', 'dis', sep='\t')

for i in range(rolls):
	d1 = random.randint(1, 20)
	d2 = random.randint(1, 20)
	
	# Normal rolls
	if d1 >= dc_5: norm_5_successes += 1
	if d1 >= dc_10: norm_10_successes += 1
	if d1 >= dc_15: norm_15_successes += 1
	
	# Advantage rolls
	if d1 >= dc_5 or d2 >= dc_5: adv_5_successes += 1
	if d1 >= dc_10 or d2 >= dc_10: adv_10_successes += 1
	if d1 >= dc_15 or d2 >= dc_15: adv_15_successes += 1
	
	# Disadvantage rolls
	if d1 >= dc_5 and d2 >= dc_5: dis_5_successes += 1
	if d1 >= dc_10 and d2 >= dc_10: dis_10_successes += 1
	if d1 >= dc_15 and d2 >= dc_15: dis_15_successes += 1
	
print(dc_5, norm_5_successes / rolls, adv_5_successes / rolls, 
	dis_5_successes/rolls, sep='\t')
print(dc_10, norm_10_successes / rolls, adv_10_successes / rolls, 
	dis_10_successes / rolls, sep='\t')
print(dc_15, norm_15_successes / rolls, adv_15_successes / rolls, 
	dis_15_successes / rolls, sep='\t')
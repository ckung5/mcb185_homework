# 55colorname.py by Clarissa Kung

import sys

colorfile = sys.argv[1]
R = int(sys.argv[2])
G = int(sys.argv[3])
B = int(sys.argv[4])
input_rgb = [R, G, B] # list P in dtc

# taxicab distance to find distance between input and file color 
def dtc(P, Q):
	d = 0
	for p, q in zip(P, Q):
		d += abs(p - q)
	return d

with open(colorfile, 'rt') as fp:
	closest_color = 0
	max_dist = 765 # white: 255 * 3
	for line in fp:
		cols = line.split()
		color = cols[0]
		vals = cols[2].split(',')
		r_val = int(vals[0])
		g_val = int(vals[1])
		b_val = int(vals[2])
		colorfile_rgb = [r_val, g_val, b_val] # list Q in dtc
		
		dist = dtc(input_rgb, colorfile_rgb)
		if dist < max_dist:
			max_dist = dist
			closest_color = cols[0]
			
print(closest_color)
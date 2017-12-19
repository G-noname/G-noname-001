#!/usr/bin/env python3

import sys

def Hours(m):
	h = m // 60
	mm = m % 60
	print("{} H, {} M".format(h, mm))

if __name__ == '__main__':
	if len(sys.argv[:]) > 2:
		exit()
	else:
		try:
			m = int(sys.argv[1])
			if m < 0:
				raise ValueError
			else:
				Hours(m)
		except(ValueError):
			print('ValueError: Input number cannot be negative')
		

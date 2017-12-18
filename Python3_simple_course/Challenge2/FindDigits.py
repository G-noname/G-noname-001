#!/usr/bin/env python3

with open('/home/shiyanlou/Code/String.txt') as f:
	s = f.read()
	a = []
	for x in s[:]:
		if x.isdigit():
			a.append(x)
		else:
			pass
for y in a:
	print(y, end='')

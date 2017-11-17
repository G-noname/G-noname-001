#!/usr/bin/env python3

def js(input):
	list=input.split(':')
	num=list[0]
	a=int(list[1])
	b=0.08+0.02+0.005+0+0+0.06
	c=3500
	z=a*(1-b)-c
	if z<=0:
		t=0
	elif z<=1500:
		t=z*0.03
	elif z<=4500:
		t=z*0.1-105
	elif z<=9000:
		t=z*0.2-555
	elif z<=35000:
		t=z*0.25-1005
	elif z<=55000:
		t=z*0.3-2755
	elif z<=80000:
		t=z*0.35-5505
	else:
		t=z*0.45-13505
	income=a*(1-b)-t
	tt=format(income,".2f")
	print(str(num)+':'+tt)

import sys

if __name__=='__main__':
	try:
		for arg in sys.argv[1:]:
			js(arg)
	except:
		print("Parameter Error")

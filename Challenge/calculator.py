#!/usr/bin/env python3
import sys

a=0
b=0
c=3500
x1=0.03
y1=0
x2=0.1
y2=105
x3=0.2
y3=555
x4=0.25
y4=1005
x5=0.3
y5=2755
x6=0.35
y6=5505
x7=0.45
y7=13505
if __name__=='__main__':
	a=int(sys.argv[1])
	try:
		z=a-b-c
		if z<=1500:
			yjse=z*x1-y1
		elif z<=4500:
			yjse=z*x2-y2
		elif z<=9000:
			yjse=z*x3-y3
		elif z<35000:
			yjse=z*x4-y4
		elif z<55000:
			yjse=z*x5-y5
		elif z<80000:
			yjse=z*x6-y6
		else:
			yjse=z*x7-y7
		tt=format(yjse,".2f")
		print(tt)	
	except:
		print("Paramenter Error")	


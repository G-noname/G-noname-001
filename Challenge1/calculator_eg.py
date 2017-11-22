#!/usr/env python3
improt sys


def main():
	if len(sys.argv)!=2:
		print('Parameter Error')
		exit()
	try:
		income = int(sys.argv[1])
	except ValueError:
		print('Parameter Error')
		exit()
	value = income - 3500
	if value <= 0:
		result =0
	elif value<=1500:
		result = value*0.03 -0
	elif value<-4500:
		result = value*0.1 -105
	elif value<=9000:
		result = value * 0.2 -555
	elif value<=35000:
		result = value*0.25 -1005
	elif value<=55000:
		result = value*0.3 -2755
	elif value<=80000:
		result = value*0.35 - 5505
	else:
		result = value*0.45 -13505
	print('{:.2f}'.format(result)


if _name__=='__main__':
	main()

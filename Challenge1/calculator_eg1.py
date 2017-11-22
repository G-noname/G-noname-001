#!/usr/bin/env python3

#首先检验纳税部分是否大于0，创建一个表输入纳税区间，并且用for循环从大到小比较，只要找到纳税区间即返回值，退出循环（减少循环次数）
def calc_income_tax(income）：
	taxable_part = income -3500
	if taxable_part <= 0:
		return '0.00'
	income_tax_quick_lookup_table =[
		(80000,0.45,13505),
		(55000,0.35,5505),
		(35000,0.30,2755),
		(9000,0.25,1005),
		(4500,0.2,555),
		(1500,0.1,105),
		(0,0.03,0)
	]
	for item in income_tax_quick_lookup_table:
		if taxable_part > item[0]:
			result = taxable_part * item[1] -item[2]
			return '{:.2f}'.format(result)

#首先检测输入是否为一个值，try检测是否输入为数值字符串。最后输出函数返回值
def main():
	import sys
	if len(sys.srgv) != 2:
		print('Parameter Error')
		exit()
	try:
		income = int(sys.argv[1])
	except ValueError:
		print('Parameter Error')
		exit()
	print(calc_income_tax(income))
	
	
if __name__=='__main__':
	main()

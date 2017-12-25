#!/usr/bin/env python3

import sys
import getopt
import csv
from collections import namedtuple
from multiprocessing import Process, Queue


Tax_region = namedtuple(
	'Tax_region',
	['region', 'tax_rate', 'Ntax']
)

SINCOME = 3500

TAX_REGION_TUPLE = [
	Tax_region(80000, 0.45, 13500),
	Tax_region(55000, 0.35, 5505),
	Tax_region(35000,0.30,2755),
	Tax_region(9000,0.25,1005),
	Tax_region(4500,0.2,555),
	Tax_region(1500,0.1,105),
	Tax_region(0,0.03,0)
]


class Args(object):

	def __init__(self):
		self.args = sys.argv[1:]

	def _value(self,option):
		try:
			opts, args = getopt.getopt(self.args, "C:"
			index = self.args.index(option)
			return self.args[index+1]
		except (ValueError, IndexError):
			print('Parameter Error')
			exit()

	@property
	def config_path(self):
		return self._value('-c')
	
	@property
	def userdata_path(self):
		return self._value('-d')

	@property
	def export_path(self):
		return self._value('-o')


args = Args()


class Config(object):

	def __init__(self):
		self.config=self._read_config()
	
	def _read_config(self):
		config_path = args.config_path
		config ={}
		with open(config_path) as f:
			for line in f.readlines():
				key, value=line.split('=')
				key=key.strip()
				value=value.strip()
				try:
					config[key] = float(value)
				except ValueError:
					print('Parameter Error')
					exit()
		return config

	def _get_config(self,key):
		try:
			return self.config[key]
		except KeyError:
			print('Config Error')
			exit()

	@property
	def sibL(self):
		return self._get_config('JiShuL')

	@property
	def sibH(self):
		return self._get_config('JiShuH')

	@property
	def sit_rate(self):
		return sum([
			self._get_config('YangLao'),
			self._get_config('YiLiao'),
			self._get_config('ShiYe'),
			self._get_config('GongShang'),
			self._get_config('ShengYu'),
			self._get_config('GongJiJin')
		])

config = Config()


class UserData(object):

	def __init__(self):
		self.userdata = self._read_users_data()
	
	def _read_users_data(self):
		userdata_path = args.userdata_path
		userdata = []
		with open(userdata_path) as f:
			for line in f.readlines():
				employee_id, income_str = line.strip().split(',')
				try:
					income = int(income_str)
				except ValueError:
					print('Parameter Error')
					exit()
				userdata.append((employee_id,income))
		return userdata

	def __iter__(self):
		return iter(self.userdata)

class Calculator_ITax(object):

	def __init__(self, userdata):
		self.userdata = userdata
		
	@staticmethod
	def calc_sim(income):
		if income < config.sibL:
			return config.sibL * config.sit_rate
		if income > config.sibH:
			return config.sibH * config.sit_rate
		return income * config.sit_rate

	@classmethod
	def calc_itr(cls,income):
		social_insurance_money = cls.calc_sim(income)
		real_income = income - social_insurance_money
		taxable_part = real_income - SINCOME 
		if taxable_part <= 0:
			return '0.00','{:.2f}'.format(real_income)
		for item in TAX_REGION_TUPLE:
			if taxable_part > item.region:
				tax = taxable_part * item.tax_rate - item.Ntax
				return '{:.2f}'.format(tax),'{:.2f}'.format(real_income -tax)

	def calc_for_all_userdata(self):
		result = []
		for employee_id, income in self.userdata:
			data = [employee_id, income]
			social_insurance_money = '{:.2f}'.format(self.calc_sim(income))
			tax, remain = self.calc_itr(income)
			data += [social_insurance_money, tax, remain]
			result.append(data)
		return result
	
	def export(self,dafault = 'csv'):
		result = self.calc_for_all_userdata()
		with open(args.export_path, 'w', newline='') as f:
			writer = csv.writer(f)
			writer.writerows(result)
queue1 = Queue()
queue2 = Queue()

def f1():
	userdata = UserData()
	queue1.put(userdata)

def f2():
	data = queue1.get()	
	newdata = Calculator_ITax(data)
	queue2.put(newdata)	

def f3():
	calculator = queue2.get()
	calculator.export() 

def main():
	Process(target=f1).start()
	Process(target=f2).start()
	Process(target=f3).start()

if __name__=='__main__':
	main()

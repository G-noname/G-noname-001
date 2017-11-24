#!/usr/bin/env python3

import sys,csv

from collections import namedtuple


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
		self._config=self._read_config()
	
	def _read_config(self):
		config_path = args.config_path
		congfig ={}
		with open(config_path) as f:
			for line in f.readlines:
				key,value=line.split('=')
				key=str1[0].strip()
				value=str1[1].strip()
				self._config[key]=value
	def get_config(self):
		return self._config

class UserData(object):
	def __init__(self):
		self.userdata={}
		with open(userdatafile) as f:
			for line in f:
				str2=line.split(',')
				key=str2[0].strip()
				value=str2[1].strip()
				self.userdata[key]=value
	def calculator(self):
		JiShuL=float(self._config[JiShuL])
		JiShuH=float(self_config[JiShuH])
		b=0
		for x in self._config.value:
			x=float(x)
			b=b+x
		b=b-JiShuL-JiShuH
		c=3500
		for i in self.userdate.key:
			a=int(self.userdata[i])
			if a<=JiShuL :
				a=JiShuL
			elif a>=JiShuH:
				a=JiShuH
			else:
				pass
			s=format(a*b,".2f")
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
			tt=format(t,".2f")
			ic=a*(1-b)-t
			income=format(ic,".2f")
			self.userdata[i]=(i+','+str(a)+','+s+','+tt+','+income) 

	def dumptofile(self,outputfile):
		with open(outputfile,'w') as f:
			for y in self.userdate:
				f.write(self.userdate[y])


if __name__=='__main__':
	if len(sys.argv) <= 2:
		print('Parametor Error')
		exit()
	args=sys.argv[1:]
	index=args.index('-c')
	configfile=args[index+1] 
	index=args.index('-d') 
	userdatafile=args[index+1] 
	index=args.index('-o') 
	outputfile=args[index+1] 
	if os.path.isfile(configfile) and os.path.isfile(userdatafile) and os.path.isfile(outputfile): 
		config=Config()
		config.get_config
		userdata=UserData()
		userdata.calculator()
		userdata.dumptofile()
	else:
		print('file is not exist') 


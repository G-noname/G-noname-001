#!/usr/bin/env python3

class Config(object):
	def __init__(self,configfile):
		self._config={}
		with open(configfile) as file:
			for line in file:
				str1=line.strip().split('=')
				key=str1[0]
				value=str1[1]
				self._config[key]=value
	def get_config(self):
		return self._config
class UserData(object):
	def __init__(self,userdatafile):
		self.userdata={}
		with open(userdatafile) as file:
			for line in file:
				str2=line.strip().split(',')
				key=str2[0]
				value=str2[1]
				self.userdata[key]=value
	def calculator(self):
		JiShuL=int(self._config[JiShuL])
		JiShuH=int(self._config[JiShuH])
		b=0
		for x in self._config.value:
			x=int(x)
			b=b+x
		b=b-JiShuL-JiShuH
		c=3500
		for i in self.userdate:
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
		with open(outputfile,'w') as file:
			for y in self.userdate:
				file.write(self.userdate[y])

import sys,os,json	

if __name__=='__main__':
	args=sys.argv[1:]
	index1=args.index('-c')
	configfile=args[index1+1] 
	index2=args.index('-d') 
	inputfile=args[index2+1] 
	index3=args.index('-o') 
	outputfile=args[index3+1] 
	try:
		if os.path.isfile(configfile) and os.path.isfile(inputfile) and os.path.isfile(outputfile): 
			config=Config(js)
			config.get_config
			userdata=Userdata(js)
			userdata.calculator()
			userdata.dumptofile()
		else:
			print('file is not exist') 
	except: print('ERROR')


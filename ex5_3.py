#!/usr/bin/env python3

class Animal(object):
	def __init__(self,name):
		self._name=name
	@property
	def name(self):
		return self._name
	@name.setter
	def name(self,value):
		self._name=value
	def make_sound(self):
		pass

class Cat(Animal):
	def make_sound(self):
		print(self.get_name() + ' is making sound miu miu miu...')

cat=Cat('Kitty')
print(cat.name)

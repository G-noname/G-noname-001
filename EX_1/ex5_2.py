#!/usr/bin/env python3

class Animal(object):
	owner = 'jack'
	def __init__(self,name):
		self._name=name
	@classmethod
	def get_owner(cls):
		return cls.owner
	def get_name(self):
		return self._name.lower().capitalize()
	def set_name(self,value):
		self._name=value  #?
	def make_sound(self):
		pass

class Dog(Animal):
	def make_sound(self):
		print(self.get_name() + ' is making sound wang wang wang...')
	
class Cat(Animal):
	def make_sound(self):
		print(self.get_name() + ' is making sound miu miu miu...')
#main function
#dog=Dog('wangcai')
#cat=Cat('kitty')
#dog.make_sound()
animals = [Dog('wangcai'),Cat('kitty'),Dog('laifu'),Cat('Betty')]
for animal in animals:
	animal.make_sound()
print(Animal.owner)
print(Cat.owner)
print(Animal.get_owner())
print(Cat.get_owner())

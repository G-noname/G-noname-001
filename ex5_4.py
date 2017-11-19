#!/usr/bin/env python3

class Animal(object):
	owner = 'jack'
	def __init__(self,name):
		self._name=name

	@staticmethod
	def order_animal_food():
		print('ording...')
		print('ok')

Animal.order_animal_food()


class Animal():
	pass
	
class Dog(Animal):
	
	def __init__(self, name):
		self.name = name
		
class Cat(Animal):
	
	def __init__(self, name):
		self.name = name
		
class Person():

	def __init__(self, name):
		self.name = name
		
		self.pet = None
		
class Employee():
	
	def __init__(self, name, sarary):
		super(Employee, self).__init__(name)
		self.sarary = sarary
		
class Fish():
	pass

class Salmon(Fish):
	pass
	
class Halibut(Fish):
	pass
	
rover = Dog("Rover")

satan = Cat("Satan")

mary = Person("Mary")


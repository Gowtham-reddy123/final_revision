#starting oops concept again with basics 
print("we should know about class ")

class Car:
	def __init__(self,brand,year):
		self.brand=brand
		self.year=year
	def drive(self,speed):
		print(self.brand,"is driving at ", speed ," in km/hr")
c=Car("toyata innova crysta",2023)
c.drive(100)
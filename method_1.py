print('''	Method:
			
			1.method is also a function and usually use self keyword in python and this in c++ and java
			
			2.it is associated with an object or class
			
			3.It is defined inside the class and usually acts on the object data
		
		KEY POINTS OF METHOD :
		
			1.Requires a class and usually uses self	
			
			2.needs an object for calling
	
			3.can be used to define the behavior of the object 
			
			for example:
			''')
class Calculator:
	def add(self,a,b):
		return a+b
		
c=Calculator()
result=c.add(13412412,412124124)
print(" 		The addition of two numbers a and b is eual to :",result)
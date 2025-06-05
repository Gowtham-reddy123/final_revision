import math 

try:
	num=int(input("enter the number : "))
	if num < 0:
		raise ValueError("square root of negative number is not allowed ")
	result=math.sqrt(num)
	print("the square root given number is : ",result)
except ValueError:
	print("please enter the input in correct manner so that we can recognize ") 
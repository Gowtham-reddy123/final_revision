try:
	celsius=float(input("enter the temperature in Celsius : "))
	if celsius<-273.15:
		raise ValueError("Minimum temperature is -273.15 after that it doesn't exists so the error will come")
	fahrenheit = (celsius * 9/5 ) + 32
	print(celsius,"celsius is equal to ",fahrenheit,"fahrenheit ")
except ValueError:
	print("invalid input ")  



print(''' 		At first python or console goes to try block and checks that error
 
			is there or not after that when we think deeply python  also don"t

		        know some errors so we have to say the python that it is an error
 
			because it is a universal truth and then we use raise key word
 

			USES OF RAISE KEYWORD :

		      1.The raise keyword is used to raise the error manually that python dont know 
		      2.This will stop the program
		      3.to enforce rules in your code
	              4.stops the programm when something is wrong
	
	 After that it converts celsius into farenheit 
	 if there is an valueError it goes to except block and prints the print statement of except block
''')
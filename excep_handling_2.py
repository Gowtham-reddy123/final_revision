try:
	s=str(input("enter the number :"))
	num=int(s)
	print("Strings are converted into number : ",num)
except ValueError:
	print("The given input is invalid and not a number ")


print(''' At first it goes to try block and check is there any error in it 
	 for example if we take 
	
                     20 as input→⇒in s it converts→⇒'20'
			after that it converts string into
			num because of conversion
	 there is no error rised so it wont go to exception block
			
			
''')
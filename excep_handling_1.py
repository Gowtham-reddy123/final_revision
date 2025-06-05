List=[1,2,3,4,5]
try:
	index=int(input("enter the index :"))
	print("enter the index you want : ",List[index])
except ValueError:
	print("please give the valid input ")
except IndexError:
	print("the index is out of range ")

print(''' At first we give list out of the block and after that we write our doubtable code in try block ,The flow of the code is 
	 step_1= first list is assigned and goes to try block if there is no error as per user input then it gives 
	 output as usual 
	 step_2=if the error arises in try block then the console goes to exception block and we should know the syntax 
	 of exception
					except <error_name>:
						block
		is the syntax it goes to exeception block asper the error 
																	
''')

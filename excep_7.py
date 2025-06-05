try:
	age=int(input("enter your age : "))
	if age < 0:
		raise ValueError
	elif age<4:
		price=100
	elif age<=18
		price=200
	else:
		price=300
	print("Ticket price is : ",price)
except ValueError as e:
	print("Invalid input    ",e)
List=[10,20,30,40,50,60,70]
try:
	element=int(input(" Enter the elements to remove from the list : "))
	List.remove(element)
	print("the updated list is given now : ",List)
except ValueError:
	print("the element you want to delete is not in the list please refer once and remove ")
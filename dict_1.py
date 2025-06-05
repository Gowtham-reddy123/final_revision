#dictionary
student_number=int(input("enter the student_no : "))
subject=str(input("enter the subject 	       : "))
marks  =str(input("enter the marks   	       : ")).split( )
print(marks)
sum=0
for x in marks:
	sum+=int(x)
average=sum/int(subject)
	
print( "Total marks awarded 	     	       : ",sum)
print(" Average alloted     	     	       : ",average)	


def decorator(main_function):
	def submain():
		print("Before main function ")
		main_function()
		print("after the main function ")
	return submain

@decorator

def hello():
	print("Hello" , " how are you ? ")
hello()
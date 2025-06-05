def f1():
	yield 1
	yield 2
	yield 3
	return f1()
result=f1()
for value in result:
	print(value)
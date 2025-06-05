def f1():
	for i in range(10):
		yield i
result=f1()
print(result.__next__())
print(result.__next__())
print(result.__next__())
print(result.__next__())
print(result.__next__())
print(result.__next__())

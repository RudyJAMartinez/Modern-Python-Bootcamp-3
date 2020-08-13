def divide(a,b):
	try:
		result = a/b
	except ZeroDivisionError:
		print("don't divide by zero please")
	except TypeError:
		print("a and b must be int or floats")
	else:
		print(f"{a} divided by {b} is {result}")

divide(1,2)
divide(1,0)
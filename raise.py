def colorize(text, color):
	colors = ("red", "white", "blue")
	if type(text) is not str:
		raise TypeError("text must be instance of str")
	if color not in colors:
		raise ValueError("color is invalid color")
	print(f"Printed {text} in {color}")

# This command will work
colorize("Apple", "red")

#This command will raise an error because 'green' is not in colors
colorize("Orange", "green")
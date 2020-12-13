age = input("What is your age: ")

if int(age) >= 18 and int(age) < 21:
	print("You can come in, but you need to wear a wristband.")
elif int(age) >= 21:
	print("Come on in and have a drink!")
else:
	print("You are too young. Get out of here!")
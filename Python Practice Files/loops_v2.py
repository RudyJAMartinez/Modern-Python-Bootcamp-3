for num in range(1,21):
	if num == 4 or num == 13:
		print(f"{num} is an unlucky number! Go away!")
	elif num % 2 == 0:
		print(f"{num} is an even number!")
	else:
		print(f"{num} is an odd number!")
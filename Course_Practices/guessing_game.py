import random
random_number = random.randint(1,10)

while True:
	guess = input("Guess a number between 1 and 10: ")
	guess = int(guess)
	if guess < random_number:
		print("You are too low!")
	elif guess > random_number:
		print("You are too high!")
	else:
		print("YOU WON")
		play_again = input("DO you want to play again? (y/n): ")
		if play_again == "y":
			random_number = random.randint(1,10)
			guess = None
		else:
			print("Thank you for playing!")
			break

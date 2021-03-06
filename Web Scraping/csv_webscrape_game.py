# Libraries / Modules
import requests
from bs4 import BeautifulSoup
from csv import DictReader
from random import choice

# Base url and url
base_url = "http://quotes.toscrape.com"

# Read Quotes from csv_scrape_quotes.py 
def read_quotes(filename):
	with open(filename, "r") as file:
		csv_reader = DictReader(file)
		quotes = list(csv_reader)
		return quotes

# Guessing Game
def start_game(quotes):
	quote = choice(quotes)
	remaining_guesses = 4

	print('Here is a quote:')
	print(quote['text'])

	guess = ''

	while guess != quote['author'].lower and remaining_guesses > 0:
		guess = input(f'Guesses remaining: {remaining_guesses} \n Who said this quote? ')
		
		if guess.lower() == quote['author'].lower():
			print("You got it right!")
			break
		remaining_guesses -= 1
		if remaining_guesses == 3:
			res = requests.get(f"{base_url}{quote['bio_link']}")
			soup = BeautifulSoup(res.text, 'html.parser')
			birth_date = soup.find(class_ = 'author-born-date').get_text()
			location = soup.find(class_ = 'author-born-location').get_text()
			print(f"Here's a hint: The author was born on {birth_date} {location}")
		elif remaining_guesses == 2:
			print(f"Here's a hint: The author's first name starts with: {quote['author'][0]}")
		elif remaining_guesses == 1:
			last_initial = quote['author'].split(" ")[1][0]
			print(f"Here's a hint: The author's last name starts with the letter: {last_initial}")
		else:
			print(f"Sorry, you ran out of guesses. The answer was: {quote['author']}") 

	again = ''
	while again not in ('y', 'yes', 'n', 'no'):
		again = input("Would you like to play again (y/n)?: ")
	if again.lower() in ('yes', 'y'):
		return start_game(quotes)
	else:
		print("Ok, goodbye now!")

quotes = read_quotes("quotes.csv")
start_game(quotes)
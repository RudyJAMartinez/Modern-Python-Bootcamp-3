#imports
from pyfiglet import figlet_format
from termcolor import colored
import requests
from random import choice 

# Opening Line
opening_line = "Dad Joke 3000"
figlet_line = figlet_format(opening_line)
colored_line = colored(figlet_line, color="blue", attrs=["blink"])
print(colored_line)

#Choose a topic
topic = input("Let me tell you a joke! Give me a topic: ")

#Dad Joke Request
url = "https://icanhazdadjoke.com/search"
response = requests.get(
	url,
	headers={"Accept": "application/json"},
	params = {"term": topic, "limit": 1}
).json()

num_jokes = response["total_jokes"]
results = response["results"]
if num_jokes > 1:
	print(f"I found {num_jokes} jokes about {topic}. Here is one:")
	print(choice(results)["joke"])
elif num_jokes == 1:
	print(f"I found one joke about {topic}")
	print(results[0]["joke"])
else:
	print(f"Sorry, couldn't find a joke with your term: {topic}")

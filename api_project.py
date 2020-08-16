#imports
from pyfiglet import figlet_format
from termcolor import colored
import requests
from random import randint 

# Opening Line
opening_line = "Dad Joke 3000"
figlet_line = figlet_format(opening_line)
colored_line = colored(figlet_line, color="blue", attrs=["blink"])
print(colored_line)

#Choos a topic
topic = input("Let me tell you a joke! Give me a topic: ")

#Dad Joke Request
url = "https://icanhazdadjoke.com/search"
response = requests.get(
	url,
	headers={"Accept": "application/json"},
	params = {"term": topic, "limit": 1}
)
json_data = response.json()

#Dad Joke 
print(f"Here's a joke about {topic}: {json_data['results']}")
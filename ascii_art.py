from pyfiglet import figlet_format 
from termcolor import colored

message = input("What message do you want to print?: ")
color = input("What color?: ")

print(colored((figlet_format(message)),color=color))
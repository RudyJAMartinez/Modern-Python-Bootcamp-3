import termcolor

text = termcolor.colored("Hello there!", color="white", on_color="on_blue",attrs=["blink"])
print(text)

print(help(termcolor))
from csv import reader
from csv import DictReader

# Print each row of the data
with open("fighters.csv") as file:
	csv_reader_1 = reader(file)
	for row in csv_reader_1:
		print(row)

# Turn the data into a list
with open("fighters.csv") as list_fighters:
	csv_reader_2 = reader(list_fighters)
	data_1 = list(csv_reader_2)
	print(data_1)

# Turn data into a dictionary
with open("fighters.csv") as dict_fighters:
	csv_reader_3 = DictReader(dict_fighters)
	for row in csv_reader_3:
		print(row)
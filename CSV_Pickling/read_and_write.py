from csv import reader, writer

with open("read_and_write.csv") as file:
	csv_reader = reader(file)
	fighters = [[s.upper() for s in row]for row in file]
	for row in fighters:
		print(row)

with open("read_and_write_2.csv", "w") as file:
	csv_writer = writer(file)
	for fighter in fighters:
		csv_writer.writerow(fighter)

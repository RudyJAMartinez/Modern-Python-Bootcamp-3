from csv import writer

# Writes the specified line into the specified file
with open("fighters.csv","w") as file:
	csv_writer = writer(file)
	csv_writer.writerow(["Rudy Martinez"])

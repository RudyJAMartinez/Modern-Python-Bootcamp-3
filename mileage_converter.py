print("How many kilometers did you run today?")
kms = input()
miles = float(kms)/1.60934
miles = round(miles,2)
print(f"You ran {kms} kilometers or {miles} miles today!")

round(miles,2)
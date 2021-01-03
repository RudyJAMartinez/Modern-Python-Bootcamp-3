import re 

def extract_phone(input):
	phone_regex = re.compile(r'\d{3} \d{3}-\d{4}')
	match = phone_regex.search(input)
	return match.group()

print(extract_phone("Call me at 415 555-4242"))

def is_valid_phone(input):
	phone_regex = re.compile(r'\d{3} \d{3}-\d{4}')
	match = phone_regex.fullmatch(input)
	if match:
		return True
	return False

print(is_valid_phone("432 567-9877"))
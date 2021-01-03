import re 

pattern = re.compile(r'\d{3} \d{3}-\d{4}')

res_1 = pattern.search('Call me at 415 555-4242')

print(res_1.group())

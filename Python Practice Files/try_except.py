def get(d,key):
	try:
		return d[key]
	except KeyError:
		return None
d = {"name": "ricky"}
print(get(d, "name"))
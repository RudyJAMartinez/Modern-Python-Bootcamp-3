from random import random

#option 1
def flip_coin1():
	r = random()
	if r > 0.5:
		return 'Heads'
	else:
		return 'Tails'

print(flip_coin1())

#option 2
def flip_coin2():
	if random() > 0.5:
		return 'Heads'
	else:
		return 'Tails'

print(flip_coin2())

# myfuncs

T_zero = 273.15



def heaviside(x):
	"""Heaviside step function Theta(x)"""
	theta = None
	if x < 0:
		theta = 0
	elif x == 0:
		theta = .5
	else:
		theta = 1

	return theta

def fahrenheit2kelvin(temp_F):
	"""Convert temp_F in F to Kelvin"""
	temp_K = (5/9)*(temp_F - 32) + T_zero
	return temp_K									# Alternatively, you can just return the expression itself

def kelvin2celsius(temp_K):
	"""Convert T in Kelvin to C"""
	temp_C = temp_K - T_zero
	return temp_C

def fahrenheit2celsius(temp_F):
	"""Convert temp_F to C"""
	return kelvin2celsius(fahrenheit2kelvin(temp_F))
	
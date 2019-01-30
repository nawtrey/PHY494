#Heaviside step function

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

x_values = [-3, 0, 3, -89, .001, 500]
y_values = []

for x in x_values:							#theta = heaviside(x)
	y_values.append(heaviside(x))			#y_values.append(theta) **Alternative for current code 

print(x_values)
print(y_values)

#This program adds a temperature difference in Farenheit to an absolute temperature in Kelvin

T_initial = float(input("Please insert an initial temperature (in Kelvin): "))	#Initial temperature in Kelvin
DeltaTheta = float(input("Please insert the temperature change (in degrees Farenheit): "))	#Temperature change in degrees Farenheit

T_final = T_initial + (5/9)*(DeltaTheta)			#Final temperature calculation in Kelvin

print("The calculated final temperature is:", T_final)
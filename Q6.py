""" 
find the volume of sphere
"""
PI = 3.14

def volumeOfSphere(radius):
	return (4/3 * PI * (radius)**3)


radius = int(input("Enter the radius value: "))
print(volumeOfSphere(radius))
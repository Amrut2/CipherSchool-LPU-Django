""" 
count the digits 

ex = 3454 has 4 digits

"""

def considerString(num):
	return (len(list(num)))
	# lst = list(num)
	# return (len(lst))

num = input("Enter the number: ")
print(considerString(num))


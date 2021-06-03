""" 
reverse a string

amrut = turma

"""

######################################################

def reversestring_slice(string):
	return string[::-1]


string = input("Enter any string: ")
res1 = reversestring_slice(string)


######################################################

def reverse_logic(string):
	# Empty string
	st = ""
	for i in string:
		st = i + st
	return st

print(reverse_logic(string))

"""

read s , index n , character c, 

hello , 0, j = jello

"""

def convert(string ,n ,c):
	return (string.replace(string[n] , c))


string = input("Enter any string: ")
n = int(input("Enter index : "))
c = input("Enter character: ")


print(convert(string ,n,c))

import math

def roots(a,b,c):
	d = (b*b) - 4*(a*c)
	# square root of discrminant using method math.sqrt()
	squarerootofd = math.sqrt(abs(d))

	if d>0:
		print((-b + squarerootofd)/(2 * a))
		print((-b - squarerootofd)/(2 * a))

	elif d == 0:
		print(-b / (2 * a))

	else:
		print("Complex roots")




a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

print(roots(a,b,c))



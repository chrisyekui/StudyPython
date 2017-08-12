def power(x,n):

	y=1
	while n>0:
		y = x * y
		n=n-1
	return y

power(5,3)
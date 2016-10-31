#! usr/bin/env python

def fibonacci(n):
	if n == 0 or n ==1:
		return 0
	else:
		 return fibonacci(n-1) + fibonacci(n-2)

for i in range(100):
	fibonacci(i)
	print(i)

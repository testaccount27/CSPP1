# Exercise: Assignment-1
# Write a Python function, factorial(n), that takes in one number and returns the factorial of given number.

# This function takes in one number and returns one number.


def factorial(n):
	'''
	n is positive Integer

	returns: a positive integer, the factorial of n.
	'''
	# Your code here
	if n==0:
		return 1
	return n * factorial(n - 1)
	


def main():
	data = input()
	for _ in range(int(data)):
		user_input = input()
		print(factorial(int(user_input)))	

if __name__== "__main__":
	main()
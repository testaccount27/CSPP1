'''
1. Exercise: Assignment-1
2. Write a Python function, factorial(n), that takes in one number
    and returns the factorial of given number.
3. This function takes in one number and returns one number.
'''
def factorial(number):
    '''
    n is positive Integer

    returns: a positive integer, the factorial of n.
    '''
    # Your code here
    if number == 0:
        return 1
    return number * factorial(number - 1)
    


def main():
    '''
    Main function
    '''
    data = input()
    for _ in range(int(data)):
        user_input = input()
        print(factorial(int(user_input)))

if __name__ == "__main__":
    main()

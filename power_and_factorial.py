# Todo : find the power of the numbers
def power(n,p):
    if p == 0 :
        # ! we return 1 as for the process of multiplying it with 2**0
        return 1
    else:
        return n * power(n,p-1)    

print('the power 2 to 3rd is {}'.format(power(2,3)) )       



def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)    

print('the factorial of {} is {}'.format(5,factorial(5))  )      
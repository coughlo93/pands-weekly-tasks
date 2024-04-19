# Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.
# You should create a function called <tt>sqrt</tt> that does this.
# $ python squareroot.py.
# Please enter a positive number: 14.5.
# The square root of 14.5 is approx. 3.8.

# Putting the input as a Float

x = float(input('Input positive floating-point number: '))

# Using addition to check if the input number is a positive number.

if x < 0:
    print ("Input is a negative number.")
    
    # Using abs() module to change a number from negative to positive.

    x = abs(x)
    print ("I'll fix it for you:", x)

def sqrt(x):
        # The variable 'n' represents an initial guess in the first iteration, equating to the number we aim to find the square root of.
        n = x 
        # In the while loop, we assess the convergence condition by:
        # 1) Verifying that the values of 'x' in two consecutive iterations are nearly identical; considering that the difference could be positive or negative, we utilize the absolute value.
        # 2) Ensuring that the value of 'x*x - n' approaches zero.
        
        while abs(x*x - n) > 0.001:
            # This is the formula used to calculate the square root by the Newton-Raphson method.

            x = x - ((x*x - n)/(2*x))
        return x

# Round the floating result to 3 decimal places.

print ("The square root of ", x , "is approx. ", round(sqrt(x),3))
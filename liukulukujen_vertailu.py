"""
Comparing floating-point (decimal) numbers.
"""

"""
The function compare_floats that uses two floating point numbers and an epsilon as a parameter and returns 
information on whether the numbers are same to a sufficient degree (the parameter epsilon) as a truth value.

:EPSILON- represents a sufficiently small error tolerance, such as 0.000000001.

"""
def compare_floats(x, y, EPSILON):
    
    """
    the function compare_floats that uses two floating point numbers and an epsilon as a parameter and returns
    information on whether the numbers are same to a sufficient degree (the parameter epsilon) as a truth value.
    
    Parameters:
    :x- represents first floating point number
    :y- represents second floating point number
    :EPSILON- constant value of epsilon.
    
    Calculations:
    : subs- substitution of x and y.
    : absolute_value represents |x − y|, we have used build-in function abs to calculate |x − y|.
    
    """

    subs= x - y
    absoulte_value=abs(subs)
    
    if absoulte_value < EPSILON:
        return True
    else:
        return False

        
def main():
    """
    :EPSILON- constant value of epsilon.
    :User_input1- represents first floating point number
    :User_input2- represents second floating point number
    
    Finally passing above values in compare_floats() function and printing the result.
   
    """
    E= 0.000000001
    User_input1= float(input('Enter first floating point number: '))
    User_input2= float(input('Enter second floating point number: '))
    
    print(compare_floats(User_input1, User_input2,  E))
    
    
if __name__ == "__main__":
    main()

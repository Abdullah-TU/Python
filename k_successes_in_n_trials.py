# This code calculates the probability of getting k successes in n trials of a binomial experiment.

import numpy

def factorial(factorial):    
    # Define function to calculate factorial of a number
    
    x=[]
    
    for i in range(1, factorial+1):
        x.append(i)
    
    result1 = numpy.prod(x)
    return result1 

def prob(n,k):
    # Define function to calculate probability of getting k successes in n trials
    
    result=factorial(n)/(factorial(k)*factorial((n-k)))
    probability=result/2**n    # probability formula
    print("combination is: ", result)
    print("Probability is:", probability) 

prob(5,3)   # Example usage of the function to calculate probability of getting 3 successes in 5 trials.

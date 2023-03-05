from math import factorial


def prob(n,k):
    # Define function to calculate probability of getting k successes in n trials
    
    result=factorial(n)/(factorial(k)*factorial((n-k)))
    probability=result/2**n    # probability formula
    print("combination is: ", result)
    print("Probability is:", probability) 

prob(5,3)   # Example usage of the function to calculate probability of getting 3 successes in 5 trials.

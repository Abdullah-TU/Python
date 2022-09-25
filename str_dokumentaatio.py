"""
: Capitalization

: Creating the function capitalize_initial_letters, which uses a string as a parameter and returns it as written, with 
each word starting in upper case but the rest of the world in lower case.

"""
def capitalize_initial_letters(capital=""):
    """
    : firstly making the provided string into lower case.          
    : then using title() method to capitalize first letter of each word.
    
    """        
    x=capital.lower()
    return x.title()              
            
capitalize_initial_letters("drIVING cAR")

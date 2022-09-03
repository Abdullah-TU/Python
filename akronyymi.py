"""
Reverse the Names to Correct Order

: Implementing the function create_an_acronym, which requests a name as a parameter and returns its acronym. 
  and some other conditions...
  
"""

def create_an_acronym(lists):
    """
    : we need to split the names where comma will be found. 
    :i[0][0].upper() method makes capital of all the first letter of each word.    
    : then join() method is used to join all the first letter.
    
    """    
    
    m=lists.split()
    n=[]
    for i in m:
        n.append(i[0][0].upper())    
    return ''.join(n)               
            
create_an_acronym("central intelligence agency")

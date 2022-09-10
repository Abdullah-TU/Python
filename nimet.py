"""
: Reverse the Names to Correct Order

: In various lists of names, names are sometimes presented in reverse order, the last name before the first name, 
so that there is a comma after the last name. Create a function reverse_name, which changes a string containing such 
a name to the order, where the first name is followed with the last name.

The names are separated with a space and the comma 
as well as all unnecessary spaces are removed. The function returns the modified name.

and some other conditions......
"""

def reverse_name(lists):
    """
    : we need to split the names where comma will be found. 
    
    :strip() method removed all the "empty space".
    
    : then fulfill the conditions to findout results.
    
    """
    
    if lists.count(',')==1:
        x= lists.split(',')
        m=x[0].strip()
        n=x[1].strip()
    
    
        if n== "" and m != "":
            return m
        elif n!= "" and m == "":
            return n
        elif n== "" and m == "":
            return ""
        else:
            return "{} {}".format(n, m)
        

    elif lists.count(',')==0:
         return lists[:].strip()

"""
Triangle's angle
"""

def calculate_angle(x, y=False):
    """
    : passing optional named arguments by position to find out the third angle of triangle.
    
    Note: the sum of triangle's corner angles is 180°.
    """
    
    if y is not False :
        n=int(y)
        f=180
        m=f-(int(x)+n)
        return m
    if y is False:
        x=int(x)
        z=90-x          
        return z
        
calculate_angle(30,78)

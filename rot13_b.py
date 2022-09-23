"""
ROT13 program code template
b)
"""

def encrypt(text):
    """
    Encrypts its parameter using ROT13 encryption technology.
    :param text: str,  string to be encrypted
    :return: str, <text> parameter encrypted using ROT13
    
    """

    regular_chars   = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                       "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                       "w", "x", "y", "z"]

    encrypted_chars = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                       "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i",
                       "j", "k", "l", "m"]
    
    upper_regular_chars=[]
    upper_encrypted_chars=[]
    
    for i in regular_chars:        
        upper_regular_chars.append(i.upper())      
    
    for i in encrypted_chars:        
        upper_encrypted_chars.append(i.upper())        
    
    if (text not in regular_chars) and (text not in encrypted_chars) and (text not in upper_regular_chars) and (text not in upper_encrypted_chars):
        print(text)
    else:
        x=zip(regular_chars, encrypted_chars)
        m=tuple(x)
    
        for i, j in m:
            if i== text:
                print(j)
   

        y=zip(upper_regular_chars, upper_encrypted_chars)
        n=tuple(y)
    
        for i, j in n:
            if i== text:
                print(j)

                
def row_encryption(sentence):
    """
    Encrypts its parameter using ROT13 encryption technology.
    :param text: str,  string to be encrypted
    :return: str, <text> parameter encrypted using ROT13
    """
    z=[char for char in sentence]
   
    for i in z: 
        encrypt(i)

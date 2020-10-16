
def print_verse(x="", y=""):
    """
          In other words, write it inside triple quotes like this
          and place it right in the beginning of your program file.
          Initial comment should explain who wrote the program and
          what does it do.
    """
    if x=="cow" and y=="moo":
        print('Old MACDONALD had a farm')
        print('E-I-E-I-O')
        print("And on his farm he had a {}".format(x))
        print("E-I-E-I-O")
        print("With a {m} {m} here".format(m=y))
        print("And a {m} {m} there".format(m=y))
        print("Here a {m}, there a {m}".format(m=y))
        print("Everywhere a {m} {m}".format(m=y))
        print("Old MacDonald had a farm")
        print('E-I-E-I-O')
        print()
        
    if x=="pig" and y=="oink":  
        print('Old MACDONALD had a farm')
        print('E-I-E-I-O')
        print("And on his farm he had a {}".format(x))
        print("E-I-E-I-O")
        print("With a {m} {m} here".format(m=y))
        print("And a {m} {m} there".format(m=y))
        print("Here a {m}, there a {m}".format(m=y))
        print("Everywhere a {m} {m}".format(m=y))
        print('Old MacDonald had a farm')
        print('E-I-E-I-O')
        print()
    
      
    if x=="duck" and y=="quack":     
        print('Old MACDONALD had a farm')
        print('E-I-E-I-O')
        print("And on his farm he had a {}".format(x))
        print("E-I-E-I-O")
        print("With a {m} {m} here".format(m=y))
        print("And a {m} {m} there".format(m=y))
        print("Here a {m}, there a {m}".format(m=y))
        print("Everywhere a {m} {m}".format(m=y))
        print('Old MacDonald had a farm')
        print('E-I-E-I-O')
        print()
        
        
    if x=="horse" or y=="neigh": 
        print('Old MACDONALD had a farm')
        print('E-I-E-I-O')
        print("And on his farm he had a {}".format(x))
        print("E-I-E-I-O")
        print("With a {m} {m} here".format(m=y))
        print("And a {m} {m} there".format(m=y))
        print("Here a {m}, there a {m}".format(m=y))
        print("Everywhere a {m} {m}".format(m=y))
        print('Old MacDonald had a farm')
        print('E-I-E-I-O')
        print()
       
    if x=="lamb" or y=="baa": 
        print('Old MACDONALD had a farm')
        print('E-I-E-I-O')
        print("And on his farm he had a {}".format(x))
        print("E-I-E-I-O")
        print("With a {m} {m} here".format(m=y))
        print("And a {m} {m} there".format(m=y))
        print("Here a {m}, there a {m}".format(m=y))
        print("Everywhere a {m} {m}".format(m=y))
        print('Old MacDonald had a farm')
        print('E-I-E-I-O')    
      
    
def main():
    """Printing old  mcdonald
    calling print_verse() function by giving two parameters
    inside it. and printing according to positions
    """
    print_verse("cow", "moo")
    print_verse("pig", "oink")
    print_verse("duck", "quack")
    print_verse("horse", "neigh")
    print_verse("lamb", "baa")


if __name__ == "__main__":
    main()
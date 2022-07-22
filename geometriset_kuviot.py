"""
Geometric patterns.

"""
 
    
def square_circumference(a): 
    """
    calculation of circumference of square
    - parameter a: the length of the square's side
    """
    circumference = 4*a
    return circumference

def square_surface_area(a):
    """square
     calculation of surface area of 
     
    - parameter a: the length of the square's side
    """
    surface_area = a*a
    return surface_area
    
def rectangle_surface_area(l,w):
    """
     calculation of surface area of rectangle
     
    - parameter l: the length of the rectangle's side 1
    - parameter w: the length of the rectangle's side 2
    """
    surface_area = l * w
    return surface_area
    
def rectangle_circumference(l,w):
    """
     calculation of circumference of rectangle
     
    - parameter l: the length of the rectangle's side 1
    - parameter w: the length of the rectangle's side 2
    """
    circumference= 2 * (l + w)     
    return circumference

def circle_surface_area(a):
    """
    calculation of circumference of the circle
     
    - parameter a: the circle's radius
    """    
    import math
    
    surface_area = math.pi * (a*a)
    return surface_area
            
def circle_circumference(a):
    """
    calculation of surface area of the circle
     
    - parameter a: the circle's radius
    """
    import math
    
    circumference = 2 * math.pi * a
    return circumference        
   

def menu():
    """
    Printing a menu for user to select which geometric pattern to use in calculations.
    - Parameter: There is no parameter for the fucntion menu().
    """
    while True:
        """
        The program first prints a menu where the user can select their desired pattern or stop the program (s = square, 
        r = rectangle and q = quit). This is the menu where the user returns after performing the previously selected 
        action.If something other than n, s or q is entered, the program prints error message "Incorrect entry, try again!" 
        and returns to the pattern selection. If a negative number or a 
        
        Zero is entered as a dimension, the user is asked to re-enter the value, using the same prompt as originally.
        
        The circle is selected from the menu with the c command.
        
        In case of square, rectangle and circle have diffrence formula for the circumference and the surface area. 
        Those are calculated according to the formula.
        
        """
        answer = input("Enter the pattern's first letter or (q)uit: ")

        if answer == "s":
            square_lists =[]
            
            while True: 
                sqinput= float(input("Enter the length of the square's side: "))
                if sqinput>0.0:
                    square_lists.append(sqinput)
                    break            
    
            a=square_lists[0]
        
            print("The circumference is {:.2f}".format(square_circumference(a)))
            print("The surface area is {:.2f}".format(square_surface_area(a)))
            pass
        
        elif answer == "r":
            length_lists =[]
            while True:   
                l= float(input("Enter the length of the rectangle's side 1: "))
                if l>0.0:
                    length_lists.append(l)
                    break
                
            while True:    
                w= float(input("Enter the length of the rectangle's side 2: "))
                if w>0.0:
                    length_lists.append(w)
                    break
            
            l=length_lists[0]
            w=length_lists[1]
                        
            print("The circumference is {:.2f}".format(rectangle_circumference(l,w)))            
            print("The surface area is {:.2f}".format(rectangle_surface_area(l,w)))            
            pass
           
        
        elif answer == "c":
            
            circle_lists =[]
            while True:   
                radius= float(input("Enter the circle's radius: "))
                if radius>0.0:
                    circle_lists.append(radius)
                    break
            a=circle_lists[0]
                    
            print("The circumference is {:.2f}".format(circle_circumference(a)))                       
            print("The surface area is {:.2f}".format(circle_surface_area(a)))            
            pass       
            

        elif answer == "q":
            # empty return quits the program without killing the kernel.
            return 

        else:
            print("Incorrect entry, try again!")

        # Empty row for the sake of readability.
        print()

def main():
    menu()
    print("Goodbye!")

if __name__ == "__main__":
    main()

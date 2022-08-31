"""
COMP.CS.100 Programming 1
Bus Time Table

Let's assume that at some less inhabited area (Teisko?), buses leave for Tampere according to the 
following schedule in the list.
Design and implement a program which asks the user what time it is and prints the times for the next 
three buses, based of the entered time.
"""

def bussi(b):
    """
    Function takes the list and printing according to the need.
    """
    for i in b:
        print(i)
        

def main():
    """
    To be able to concentrate on the essential matter (presenting the schedule as a list), 
    simplify the presentation of the time by saving the time as one integer where the minutes and 
    the hours are expressed in the same number, i.e. 6:30 as 630 and 16:20 as 1620. 
    Times presented this way can easily be compared with each other
    """
    bus = [630,1015,1415,1620,1720,2000]

    bus1=[]
    bus2=[]
    bus3=[]
    bus4=[]
    bus5=[]
    bus6=[]
    bus7=[]
    bus8=[]

    enter = int(input("Enter the time (as an integer): "))


    if enter <= 630:
        bus1.extend(bus[0:3]) # extend stores multiple element in the list, but append stores only one.
      
    elif 630 < enter <= 1015: 
        bus2.extend(bus[1:4])
    
    elif 1015 < enter <= 1415:   
        bus3.extend(bus[2:5])
    
    elif 1415 < enter <= 1620:  
        bus4.extend(bus[3:6])

    elif 1620 < enter <= 1720:    
        bus5.extend(bus[4:6])    
        bus5.append(bus[0])  
    
    elif 1720 < enter <= 2000:    
        bus6.append(bus[5])
        bus6.extend(bus[0:2])
    
    elif 2000 < enter <= 2400:    
        bus7.extend(bus[0:3])

    else:    
        bus7.extend(bus[0:3]) 

    print("The next buses leave:")   

    bussi(bus1)
    bussi(bus2)
    bussi(bus3)
    bussi(bus4)
    bussi(bus5)
    bussi(bus6)
    bussi(bus7)
    bussi(bus8)

if __name__ == "__main__":
    main()
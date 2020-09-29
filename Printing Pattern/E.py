for row in range(0,7):
    for col in range(0,4):
        if ((row==0 or row==6 or col==0 )or(row==3)):
            print('#', end='')
        else:
            print( end=" ")
    print()
for row in range(0,7):
    for col in range(0,5):
        if ( col==0 or  row==6):
            print('#', end='')
        else:
            print( end=" ")
    print()
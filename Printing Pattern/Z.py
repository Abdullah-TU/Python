for row in range(0,8):
    for col in range(0,7):
        if (row+col==6) or (col==1 and row==5) or (row==0 or row==6):
            print('#', end='')
        else:
            print( end=" ")
    print()
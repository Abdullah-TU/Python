for row in range(0,7):
    for col in range(0,5):
        if (col==2 and row>1) or (row==col and col<2)or (col==4 and row<1) or (row==1 and col==3):
            print('#', end='')
        else:
            print( end=" ")
    print()
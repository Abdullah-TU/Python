for row in range(0,7):
    for col in range(0,3):
        if (( col==1  or row ==0  or row==6)):
            print('#', end='')
        else:
            print( end=" ")
    print()
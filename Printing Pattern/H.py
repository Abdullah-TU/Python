for row in range(0,7):
    for col in range(0,4):
        if ((col==0  or col==3 )or(row==3)):
            print('#', end='')
        else:
            print( end=" ")
    print()

for row in range(0,4):
    for col in range(0,7):
        if (row-col==0)or(row+col==6):
            print('#', end='')
        else:
            print( end=" ")
    print()
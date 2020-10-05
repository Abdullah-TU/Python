for row in range(0, 4):
    for col in range(0, 14):
        if (row - col == 0) or (row + col == 6):
            print('#', end='')

        elif col == 3 and (row - col == 1) or (row + col == 13) or (col == 8 and row == 1) or (col == 9 and row == 2):
            print('#', end='')

        else:
            print(end=" ")
    print()
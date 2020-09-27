"""
COMP.CS.100 Programming 1
Template for task: box printing
"""
def print_box(width, height, mark):
    """
    returning width, height, mark
    """

    for i in range(0,height):
        for j in range(0, width):
            print(f'{mark}', end='')
        print()

def main():
    """
    Firstly, taking input from user
    secondly, using nested for loop to show the structure
    """

    width = int(input("Enter the width of a frame: "))
    height = int(input("Enter the height of a frame: "))
    mark = input("Enter a print mark: ")
    print()

    print_box(width, height, mark)


if __name__ == "__main__":
    main()

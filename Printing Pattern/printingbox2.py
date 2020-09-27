
def read_input(prompt):
    number = int(input(prompt))
    return number



def main():

    while True:
        try:
            width =read_input("Enter the width of a frame: ")
        except ValueError:
            continue

        if width < 1:
            continue
        else:
            break

    while True:
        try:
            height = read_input("Enter the height of a frame: ")
        except ValueError:
            continue

        if height < 1:
            continue
        else:
            mark = input("Enter a print mark: ")
            print()
            break

    for i in range(height):
        for j in range(width):
            print(f'{mark}', end='')
        print()


if __name__ == "__main__":
    main()

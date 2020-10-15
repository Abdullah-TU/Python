# Create a program that prints the dates for all the Fridays in 2014. In 2014, the first Friday was 3.1.

def main():
    for month in range(1, 13):
        if month == 1:
            for i in range(1, 32, 7):
                i = i + 2
                print('{}.{}.'.format(i, month))

        elif month == 2:
            for i in range(1, 29, 7):
                i = i + 6
                print('{}.{}.'.format(i, month))

        elif month == 3:
            for i in range(1, 32, 7):
                i = i + 6
                while i >= 31:
                    break
                else:
                    print('{}.{}.'.format(i, month))

        elif month == 4:
            for i in range(1, 31, 7):
                i = i + 3
                while i >= 31:
                    break
                else:
                    print('{}.{}.'.format(i, month))


        elif month == 5:
            for i in range(1, 32, 7):
                i += 1
                print('{}.{}.'.format(i, month))

        elif month == 6:
            for i in range(1, 31, 7):
                i += 5
                while i >= 31:
                    break
                else:
                    print('{}.{}.'.format(i, month))


        elif month == 7:
            for i in range(1, 32, 7):
                i += 3
                while i >= 31:
                    break
                else:
                    print('{}.{}.'.format(i, month))


        elif month == 8:
            for i in range(1, 32, 7):
                while i >= 31:
                    break
                else:
                    print('{}.{}.'.format(i, month))


        elif month == 9:
            for i in range(1, 31, 7):
                i += 4
                while i >= 31:
                    break
                else:
                    print('{}.{}.'.format(i, month))


        elif month == 10:
            for i in range(1, 32, 7):
                i += 2
                while i >= 32:
                    break
                else:
                    print('{}.{}.'.format(i, month))


        elif month == 11:
            for i in range(1, 31, 7):
                i += 6
                while i >= 31:
                    break
                else:
                    print('{}.{}.'.format(i, month))

        else:
            for i in range(1, 32, 7):
                i += 4
                while i >= 31:
                    break
                else:
                    print('{}.{}.'.format(i, month))


if __name__ == "__main__":
    main()

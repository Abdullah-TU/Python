# The Fibonacci Sequence is the series of numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ..

def main():
    enter = int(input("How many Fibonacci numbers do you want? "))
    a, b = 0, 1
    c = 0
    while True:
        a, b = b, a + b
        c += 1
        if c == (enter + 1):
            break
        else:
            print("{}. {}".format(c, a))


if __name__ == "__main__":
    main()
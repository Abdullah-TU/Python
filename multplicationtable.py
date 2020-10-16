def main():
    n = int(input("Choose a number: "))
    for i in range(1, 11):
        x = i * n
        print("{} * {} = {}".format(i, n, x))


if __name__ == "__main__":
        main()

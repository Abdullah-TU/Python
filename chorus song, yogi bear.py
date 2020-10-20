def repeat_name(a, n):
    word = "Bear"
    if n == 1:
        for i in range(n):
            print(f"{a}, {a}")
    else:
        for i in range(n):
            print(f"{a}, {a} {word}")


def verse(x="", y=""):
    z = "Bear"
    if x == "I know someone you don't know" and y == "Yogi":
        print("I know someone you don't know")
        repeat_name(y, 1)
        print("I know someone you don't know")
        repeat_name(y, 3)
        print("I know someone you don't know")
        print("Yogi, Yogi Bear")
        print()

    if x == "Yogi has a best friend too" and "Boo Boo":
        print("Yogi has a best friend too")
        repeat_name(y, 1)
        print("Yogi has a best friend too")
        repeat_name(y, 3)
        print("Yogi has a best friend too")
        print("Boo Boo, Boo Boo Bear")
        print()

    if x == "Yogi has a sweet girlfriend" and y == "Cindy":
        print("Yogi has a sweet girlfriend")
        repeat_name(y, 1)
        print("Yogi has a sweet girlfriend")
        repeat_name(y, 3)
        print("Yogi has a sweet girlfriend")
        print("Cindy, Cindy Bear")
        print()


def main():

    verse("I know someone you don't know", "Yogi")
    verse("Yogi has a best friend too", "Boo Boo")
    verse("Yogi has a sweet girlfriend", "Cindy")


if __name__ == "__main__":
    main()
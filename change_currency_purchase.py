def main():
    purchase = int(input("Purchase price: "))
    paid = int(input("Paid amount of money: "))
    money = paid - purchase

    nominals = (10, 5, 2, 1)
    if purchase == paid:
        print("No change")
    elif purchase > paid:
        print("No change")
    else:
        print("Offer change:")
        coins = {}
        for coin in nominals:
            coins[coin] = money // coin
            money %= coin

        for i in coins:

            if coins[i] == 0:
                continue
            elif i == 10:
                print("%d" % coins[i] + " ten-euro notes")
            elif i == 5:
                print("%d" % coins[i] + " five-euro notes")
            elif i == 2:
                print("%d" % coins[i] + " two-euro coins")
            elif i == 1:
                print("%d" % coins[i] + " one-euro coins")
            else:
                print()


if __name__ == "__main__":
    main()
def main():
    amount_due = 50
    coins = [25, 10, 5]

    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        coin = int(input("Insert Coin: "))
        if coin in coins:
            amount_due -= coin
            if amount_due <= 0:
                print(f"change owed: {abs(amount_due)}")


if __name__ == '__main__':
    main()

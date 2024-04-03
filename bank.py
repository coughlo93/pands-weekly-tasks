def main():

    # Input the first money amount in cents
    amount1 = int(input("Enter amount1 (in cent): "))
    # Input the second money amount in cents
    amount2 = int(input("Enter amount2 (in cent): "))
    # Total amount
    total_amount = amount1 + amount2
    # Convert the total amount to euros and cents
    euros = total_amount // 100
    cents = total_amount % 100
    # Print answer
    print(f"The sum of these is €{euros}.{cents:02d}")

if __name__ == "__main__":
    main()
def main():
    
    # Input the first amount in cents
    amount1 = int(input("Enter amount 1 (in cent): "))

    # Input the second amount in cents
    amount2 = int(input("Enter amount 2 (in cent): "))

    # Calculate the total amount
    total_amount = amount1 + amount2

    # Convert to euros and cents
    euros = total_amount // 100
    cents = total_amount % 100

    # Print answer
    print(f"The sum of these is €{euros}.{cents:02d}")

if __name__ == "__main__":
    main()
    
def main():

  amount1 = int(input("Enter amount1(in cent): "))
  amount2 = int(input("Enter amount2(in cent): "))

  sum_euros = (amount1 + amount2) / 100

  print(f"The sum of these is €{sum_euros:.2f}")

if __name__ == "__main__":
  main()

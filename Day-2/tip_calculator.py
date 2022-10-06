def main():
    print("Welcome to the tip calulator.  ")
    total_bill: float = float(input("What was the total bill? $ "))
    split_into: int = int(input("How many people to split the bill? "))
    tip_percentage: int = int(
        input("What percentage tip would you like to give? 10, 12, 15 or 20? "))
    total_bill = total_bill + total_bill*tip_percentage/100
    result: float = total_bill/split_into
    print(f"Each person should pay: ${round(result, 2)}")


if __name__ == "__main__":
    main()

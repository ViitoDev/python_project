def calculate_bill():
    tip = (bill * percentage) / 100
    print(f"Tip amount is: {tip}")
    final_bill = tip + bill
    print(f"The bill, including the tip, is: {final_bill:.2f}")

bill = float(input("Enter the bill amount: \n"))
percentage = float(input("Enter the tip percentage: \n"))
calculate_bill()
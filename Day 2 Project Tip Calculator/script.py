print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? $"))
tip = int(input(
    "What percentage tip would you like to give? 10, 12 or 15? "))

people = int(input("How many people to split the bill? "))

total_bill = ((tip / 100) * bill) + bill
eachPerson = round(total_bill / people, 2)

# To see two decimal places by using format
eachPerson = "{:.2f}".format(eachPerson)


print(f"Each person should pay: ${eachPerson}")

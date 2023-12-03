print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tips = float(input("How much tip would you like to give? 10, 12, or 15?"))
no_of_persons = int(input("How many people to split the bill?"))

tips = total_bill * (tips/100)
amount_per_person = round((total_bill + tips)/no_of_persons,2)

print(f"Each person should pay: ${amount_per_person}")
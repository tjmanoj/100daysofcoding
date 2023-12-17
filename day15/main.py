MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def empty_ingredient(drink):
    if drink == "espresso":
        scarcity = "water" if resources["water"] < 50 else "coffee"
    elif drink == "latte":
        scarcity = "water" if resources["water"] < 200 else "milk"
    else:
        scarcity = "water" if resources["water"] < 250 else "milk"
    print(f"Sorry there is not enough {scarcity}")


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


def check_ingredient(drink):
    if drink == "espresso":
        if resources["water"] >= 50 and resources["coffee"] >= 18:
            return True
        return False
    elif drink == "latte":
        if resources["water"] >= 200 and resources["coffee"] >= 24 and resources["milk"] >= 150:
            return True
        return False
    else:
        if resources["water"] >= 250 and resources["coffee"] >= 24 and resources["milk"] >= 100:
            return True
        return False


def check_coins(drink):
    print("Please insert coins.")
    quarter = int(input("How many quarters?: "))
    dime = int(input("How many dimes?: "))
    nickel = int(input("How many nickles?: "))
    penny = int(input("How many pennies?: "))

    paid_amount = (quarter * 0.25) + (dime * 0.1) + (nickel * 0.05) + (penny * 0.01)
    drink_amount = MENU[drink]["cost"]

    if paid_amount > drink_amount:
        return paid_amount
    elif paid_amount == drink_amount:
        return paid_amount
    else:
        return False


def make_drink(drink):
    drink_amount = MENU[drink]["cost"]
    coins = check_coins(drink)
    if coins:
        resources["water"] -= MENU[drink]["ingredients"]["water"]
        if drink != "espresso":
            resources["milk"] -= MENU[drink]["ingredients"]["milk"]
        resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
        resources["money"] += drink_amount

        if coins > drink_amount:
            change = round((coins - drink_amount),2)
            print(f"Here is ${change} in change")
        print(f"Here is you {drink}☕. Enjoy!")

    else:
        print("Sorry that's not enough money. Money refunded!")


is_machine_on = True

while is_machine_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino):")
    if user_choice == "off":
        is_machine_on = False
    elif user_choice == "report":
        print_report()
    elif user_choice not in ["espresso", "latte", "cappuccino"]:
        print("Drink not available!!")
    else:
        availability = check_ingredient(user_choice)
        if availability:
            make_drink(user_choice)
        else:
            empty_ingredient(user_choice)


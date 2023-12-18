from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_make = CoffeeMaker()
money = MoneyMachine()
is_machine_on = True

while is_machine_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino):")
    if user_choice == "off":
        is_machine_on = False
    elif user_choice == "report":
        coffee_make.report()
        money.report()
    else:
        drink = menu.find_drink(user_choice)
        if drink:
            is_ingredient_available = coffee_make.is_resource_sufficient(drink)
            if is_ingredient_available:
                if money.make_payment(drink.cost):
                    coffee_make.make_coffee(drink)
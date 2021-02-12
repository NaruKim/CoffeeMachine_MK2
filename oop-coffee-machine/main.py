from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu=Menu()
maker=CoffeeMaker()
money=MoneyMachine()

def coffeemachineMK2():
    while True:
        choice=input(f"What do you want? {menu.get_items()} :").lower()
        if choice=="report":
            print(maker.report())
            print(money.report())
            continue
        elif choice=="off":
            print(f"The machine is off\n{money.report()}")
            return 0

        drink=menu.find_drink(choice)

        if maker.is_resource_sufficient(drink) and money.make_payment(drink.cost):
                maker.make_coffee(drink)

coffeemachineMK2()
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
menu = Menu()
coffee_maker = CoffeeMaker()


def main():
    machine_status = True
    while machine_status:

        user_request = input(f"What would you like? ({menu.get_items()}): ").lower()

        if user_request == "off":
            machine_status = False

        elif user_request == "report":
            coffee_maker.report(), money_machine.report()

        else:
            chosen_coffee = menu.find_drink(user_request)
            if coffee_maker.is_resource_sufficient(
                    chosen_coffee
            ) and money_machine.make_payment(chosen_coffee.cost):
                coffee_maker.make_coffee(chosen_coffee)


if __name__ == "__main__":
    main()

from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine


def func_main():
    if __name__ == "__main__":
        menu = Menu()
        coffee_machine = CoffeeMaker()
        money = MoneyMachine()

        is_turned_on = True
        while is_turned_on:
            user_order = input(f"What would you like? ({menu.get_items()}): ")
            if user_order == "off":
                is_turned_on = False
            elif user_order == "report":
                coffee_machine.report()
                money.report()
            else:
                ordered_menu_item = menu.find_drink(user_order)
                if ordered_menu_item is not None:
                    if coffee_machine.is_resource_sufficient(ordered_menu_item):
                        if money.make_payment(ordered_menu_item.cost):
                            coffee_machine.make_coffee(ordered_menu_item)


func_main()

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
    },
}

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resources_for_order(user_order):
    order_ingredients = MENU[user_order]["ingredients"]
    for resource in order_ingredients:
        if order_ingredients[resource] >= resources[resource]:
            print(f"Sorry there is not enough {resource}.")
            return False
    return True


def take_payment(user_order):
    order_cost = MENU[user_order]["cost"]
    print(f"A {user_order} costs ${order_cost:.2f}, please insert your coins")

    num_quarters = int(input("How many quarters will you insert ($0.25): "))
    num_dimes = int(input("How many dimes will you insert ($0.10): "))
    num_nickles = int(input("How many nickles will you insert ($0.05): "))
    num_pennies = int(input("How many pennies will you insert ($0.01): "))

    payment = (
        (0.25 * num_quarters)
        + (0.10 * num_dimes)
        + (0.05 * num_nickles)
        + (0.01 * num_pennies)
    )
    if order_cost <= payment:
        change = payment - order_cost
        print(f"Here is ${change:.2f} dollars in change")
        return True

    print("Sorry that's not enough money. Money refunded.")
    return False


def make_order(user_order):
    order_ingredients = MENU[user_order]["ingredients"]
    for resource in order_ingredients:
        resources[resource] = resources[resource] - order_ingredients[resource]

    order_cost = MENU[user_order]["cost"]
    global profit
    profit = profit + order_cost

    print(f"Here's your {user_order}.")


def report_resources():
    print("Current resources:")
    print(f"Water: {resources['water']}ml")
    print(f"Water: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")


def turn_off():
    print("The coffee machine has been turned off.")


def taking_order(user_order):
    if user_order in MENU:
        is_order_possible = check_resources_for_order(user_order)
        if is_order_possible:
            is_payment_enough = take_payment(user_order)
            if is_payment_enough:
                make_order(user_order)
                another_order = input(
                    "Would you like another order? (yes or no): "
                ).lower()
                if another_order == "yes" or another_order == "y":
                    print("\n" * 30)
                    return True
                else:
                    return False
            elif not is_order_possible:
                print("Sorry that's not enough money. Money refunded.")
        elif not is_order_possible:
            print("Please choose one of our other available options.")
            return True
    else:
        print("Please choose one of our available options.")
        return True


def func_main():
    if __name__ == "__main__":
        is_turned_on = True
        while is_turned_on:
            user_order = input(
                "What would you like? (espresso/latte/cappuccino): "
            ).lower()

            if user_order == "off":
                is_turned_on = False
                turn_off()
            elif user_order == "report":
                report_resources()
            else:
                is_turned_on = taking_order(user_order)


func_main()

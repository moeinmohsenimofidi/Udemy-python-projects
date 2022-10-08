PROFIT = 0
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
    "water": 1300,
    "milk": 1200,
    "coffee": 100,
}


def resources_are_efficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f" there is not enough {item}.")
            return False
        else:
            return True


def count_coins():
    print("Please insert coins:")
    total = int(input("How many quarters?")) * 0.25
    total += int(input("How many quarters?")) * 0.1
    total += int(input("How many quarters?")) * 0.05
    total += int(input("How many quarters?")) * 0.01
    return total


def transaction_successful(money, cost):
    if money >= cost:
        change = round(money - cost, 2)
        print(f"Here is ${change} in change.")
        global PROFIT
        PROFIT += cost
        return True
    else:
        print("Sorry that is not enough money,money is refund.")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} coffee☕")


def coffee_machine():
    is_on = True
    should_continue = True
    payment = 0
    while should_continue:
        while is_on:
            choice = input("What would you like?  (Espresso// Latte // Cappuccino) ").lower()
            if choice == "off":
                is_on = False
                print("Thank you for your try,maybe next time.")
            elif choice == "report":
                print(f" WATER : {resources['water']} ml\n Milk: {resources['milk']} ml\n Coffee: {resources['coffee']} g")
                print(f" Profit : {PROFIT}")
            else:
                drink = MENU[choice]
                if resources_are_efficient(drink["ingredients"]):
                    payment = count_coins()
                    if transaction_successful(payment, drink['cost']):
                        make_coffee(choice, drink["ingredients"])

                        repeat = input("Do you want to continue: 'Y or 'N\n").lower()
                        if repeat == "y":
                            coffee_machine()
                        elif repeat == "n":
                            should_continue = False
                            print("GOOD LUCK")


coffee_machine()

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
}

profit = 0


def resources_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            return False
    return True


def money_sufficient(cost):
    print("please insert coins")
    total_money = int(input("How many quarters?")) * 0.25
    total_money += int(input("How many dimes?")) * 0.1
    total_money += int(input("How many pennies?")) * 0.05
    total_money += int(input("How many nickels?")) * 0.01
    if total_money >= cost:
        print("Transaction is successful")
        remaining_amount = round(total_money - cost, 2)
        print(f"The change you receive is ${remaining_amount}")
        return True
    return False


def update_resources(quantity):
    for item in quantity:
        resources[item] -= quantity[item]
    print(f"the updated resources are {resources}")


is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino):").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"""Water: {resources["water"]}ml""")
        print(f"""Milk: {resources["milk"]}ml""")
        print(f"""Coffee: {resources["coffee"]}g""")
        print(f"Money: ${profit}")
    else:
        selected = MENU[choice]
        if resources_sufficient(selected["ingredients"]):
            if money_sufficient(selected["cost"]):
                profit += selected["cost"]
                print(f"your {choice} is ready")
                print(f"The profit is ${profit}")
                update_resources(selected["ingredients"])
            else:
                print("Sorry, that's not enough money")
        else:
            print("There are no enough resources")

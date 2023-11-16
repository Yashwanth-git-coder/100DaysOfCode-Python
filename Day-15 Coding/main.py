
from art import logo

print(logo)

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

profit = 0
report = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def sufficient_resources(suffi_drink):
    for item in suffi_drink:
        if suffi_drink[item] > report[item]:
            print("Sorry, there is no Sufficient water")
            return False
    return True
def process_coin():
    print("Please insert a coin : ")
    total = int(input("how many quarters? : ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def is_transaction_successful(money_recived, cost_money):
    if money_recived >= cost_money:
        change = round(money_recived - cost_money, 2)
        print(f"Here is your change : {change}$")
        global profit
        profit += cost_money
        return True
    else:
        print("Sorry insufficient money, money refunded")
        return False

def make_coffee(drink_name, other_ingridents):
    for item in other_ingridents:
        report[item] -= other_ingridents[item]
    print(f"Here is your {drink_name},enjoy the ☕")


machine_running = True
while machine_running:
    choice = input("What would you like? (espresso/latte/cappuccino) : ")
    if choice == "off":
        machine_running = False
    elif choice == "report":
        print(f"water : {report['water']}ml")
        print(f"milk : {report['milk']}ml")
        print(f"coffee : {report['coffee']}g")
        print(f"money : {profit}$")
    else:
        drink = MENU[choice]
        if sufficient_resources(drink["ingredients"]):
            payment = process_coin()
            if is_transaction_successful(payment,drink["cost"]):
                make_coffee(choice,drink["ingredients"])


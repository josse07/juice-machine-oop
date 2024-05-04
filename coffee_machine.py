Menu = {
    "latte":{
        'ingredient':{
            'water': 200,
            'milk': 200,
            'coffee': 50,
        },
        'cost': 100
    },
    "espresso":{
        'ingredient': {
            'water': 80,
            'coffee': 10,
        },
        'cost': 150,
        
    },
    "cappuccino":{
        'ingredient':{
            'water': 200,
            'milk': 150,
            'coffee': 180,
        },
        'cost': 200,
    }
}
profit = 0
resources = {
    'water': 1000,
    'milk': 700,
    'coffee': 500,
    
}
def checkResources(ordered_ingredient):
    for item in ordered_ingredient:
        if ordered_ingredient[item]>resources[item]:
            print(f"there is not enough {item}")
            return False
    return True

def amount_needed():
    print("please insert the required money.")
    #total = 0
    inputed_amount = int(input())
    return inputed_amount

def check_money_successful(money_recieved, coffee_cost):
    if money_recieved >= coffee_cost:
        global profit
        profit += coffee_cost
        change = money_recieved - coffee_cost
        print(f"Here is your ${change} in change")
        return True
    else:
        print("Sorry your money is not enough. Money refunded")
        return False 
    
def make_coffee(coffee_name, coffee_ingredients):
    for item in coffee_ingredients:
        resources[item] -= coffee_ingredients[item]
    print(f"Here is your {coffee_name}.. Enjoy!!!")
                      
isNotOff = True
while isNotOff:
    choice = input('what would you like to have? (latte/espresso/cappuccino): ')
    if choice == "off":
        isNotOff = False
    elif choice == "report":
        print(f"Water = {resources['water']}ml")
        print(f"Milk = {resources['milk']}ml")
        print(f"Coffee = {resources['coffee']}g")
        print(f"Money = ${profit}")
    else:
        coffee_type = Menu[choice]
        print(coffee_type)
        if checkResources(coffee_type['ingredient']):
           payment = amount_needed()
           if check_money_successful(payment, coffee_type['cost']):
               make_coffee(choice, coffee_type['ingredient'])
        
        
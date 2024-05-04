class Coffee_Machine():
    def __init__(self, water_level, milk_level, sugar_level, coffee_bean_level):
        
        self.water_level = water_level
        self.milk_level = milk_level
        self.sugar_level = sugar_level
        self.coffee_bean_level = coffee_bean_level
        self.money = 0
        self.avail_coffee = ['latte','espresso','cappucino']
        self.ingredients_for_coffeeType = {
            'latte':{
                'ingredients':{
                    'water': 100,
                    'milk': 150,
                    'sugar':30,
                    'coffee_bean': 40,
                },
                'cost': 100
            },
            'espresso': {
                'ingredients':{
                    'water': 150,
                    'sugar': 50,
                    'coffee_bean': 40,
                },
                'cost': 150
            },
            'cappucino': {
                'ingredients':{
                    'water': 200,
                    'milk': 200,
                    'sugar': 40,
                    'coffee_bean': 50,
                },
                'cost': 250,
            }
        }

        
    def make_coffee (self, coffee_Type):
        if coffee_Type not in self.ingredients_for_coffeeType:
            print("We don't have your desired coffee type.")
            return False
            
        ingredients_needed = self.ingredients_for_coffeeType[coffee_Type]['ingredients']
        cost = self.ingredients_for_coffeeType[coffee_Type]['cost']
            
        enough_ingredients = True
        for ingredients, amount in ingredients_needed.items():
            if getattr(self, f'{ingredients}_level') < amount:
                enough_ingredients = False
                print(f"Not enough {ingredients} to make {coffee_Type}!!")
                return False
            
            
        if enough_ingredients:
            print('please insert the required money')
            inputed_amount = int(input())
            print(f"making {coffee_Type}...")
            for ingredients, amount in ingredients_needed.items():
                setattr(self, f"{ingredients}_level", getattr(self, f"{ingredients}_level")- amount)
            self.money += cost
            
            if inputed_amount >= cost:
                change = inputed_amount - cost
                print(f'This is your ${change} change.')
                print()
                collected_money = self.money
                print(f"Here's your {coffee_Type}! Enjoy")
                print()
                print(f"Money in the machine is ${collected_money} .")
                print()
            elif inputed_amount < cost:
                print('Your money is not sufficient for this coffee')
                print(f'your ${inputed_amount} is being refunded')
        else:
            print(f"We don't have your {coffee_Type}")
            
    def get_choice(self):
        self.name_of_coffee = input('what would you like to have? (latte/espresso/cappuccino): ')    

    def refill_water(self, amount):
        self.water_level += amount
        print(f"Water refilled by {amount} ml. Current level: {self.water_level} ml.")
    
    def refill_milk(self, amount):
        self.milk_level += amount
        print(f"Milk refilled by {amount}ml, Current level: {self.milk_level}ml")
    
    def refill_coffee_beans(self, amount):
        self.coffee_bean_level += amount
        print(f"Coffee_beans refilled by {amount}g. Current level: {self.coffee_bean_level}g.")
    
    def refill_sugar(self, amount):
        self.sugar_level += amount
        print(f"Sugar refilled by {amount}g. Current level: {self.sugar_level}g.")
            

            
    
             


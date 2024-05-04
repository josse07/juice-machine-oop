class FruitJuice_machine():
    
    def __init__(self, water_level, ice_level, milk_level, sugar_level, orange_level, banana_level, pineapple_level, lemon_level, apple_level):
        self.water_level = water_level
        self.ice_level = ice_level
        self.milk_level = milk_level
        self.sugar_level = sugar_level
        self.orange_level = orange_level
        self.banana_level = banana_level
        self.pineapple_level = pineapple_level
        self.lemon_level = lemon_level
        self.apple_level = apple_level
        self.money = 0
        self.avail_juice = ['orange juice', 'banana juice', 'pineapple juice', 'lemon juice', 'apple juice']
        self.ingredients_for_juice = {
            'orange juice':{
                'ingredients':{
                    'orange': 4,
                    'water': 15,
                    'ice': 3,
                },
                'cost': 15
            },
            'banana juice': {
                'ingredients':{
                    'banana': 10,
                    'water': 10,
                    'milk': 20,
                    'ice': 4,
                },
                'cost': 25
            },
            'pineapple juice': {
                'ingredients':{
                    'pineapple': 2,
                    'water': 12,
                    'sugar': 4,
                    'ice': 5,
                },
                'cost': 30,
            },
            'lemon juice': {
                'ingredients':{
                    'lemon': 5,
                    'water': 20,
                    'sugar': 8,
                    'ice': 10,
                },
                'cost': 25,
            },
            'apple juice':{
                'ingredients':{
                    'apple': 4,
                    'water': 15,
                    'sugar': 3,
                    'ice': 5,
                },
                'cost': 35,
            }
        }

    def make_orange_juice(self, ordered_juice):
        if ordered_juice not in self.ingredients_for_juice:
            print("We dont have the ordered juice")
            return False
        
        ingredients_needed = self.ingredients_for_juice[ordered_juice]['ingredients']
        cost = self.ingredients_for_juice[ordered_juice]['cost']
        
        enough_ingredients = True
        for ingredients, amount in ingredients_needed.items():
            if getattr(self, f'{ingredients}_level') < amount:
                enough_ingredients = False
                print(f"Not enough {ingredients} to make {ordered_juice} ")
                return False
        
        if enough_ingredients:
            print('please insert the required money')
            inputed_amount = int(input())
            print(f"making {ordered_juice}...")
            for ingredients, amount in ingredients_needed.items():
                setattr(self, f"{ingredients}_level", getattr(self, f"{ingredients}_level")- amount)
            self.money += cost
            
            if inputed_amount >= cost:
                change = inputed_amount - cost
                print(f'This is your ${change} change.')
                collected_money = self.money
                print(f"Here's your {ordered_juice}! Enjoy")
                print()
                print(f"Money in the machine is ${collected_money} .")
                print()
            
            elif inputed_amount == str or inputed_amount == float:
                print('No valid amount inputed')
                raise ValueError
            
            elif inputed_amount < cost:
                print('Your money is not sufficient for this juice')
                print(f'your ${inputed_amount} is being refunded')
                
    def make_banana_juice(self, ordered_juice):
        if ordered_juice not in self.ingredients_for_juice:
            print("We dont have the ordered juice")
            return False
        
        ingredients_needed = self.ingredients_for_juice[ordered_juice]['ingredients']
        cost = self.ingredients_for_juice[ordered_juice]['cost']
        
        enough_ingredients = True
        for ingredients, amount in ingredients_needed.items():
            if getattr(self, f'{ingredients}_level') < amount:
                enough_ingredients = False
                print(f"Not enough {ingredients} to make {ordered_juice} ")
                return False
        
        if enough_ingredients:
            print('please insert the required money')
            inputed_amount = int(input())
            print(f"making {ordered_juice}...")
            for ingredients, amount in ingredients_needed.items():
                setattr(self, f"{ingredients}_level", getattr(self, f"{ingredients}_level")- amount)
            self.money += cost
            
            if inputed_amount >= cost:
                change = inputed_amount - cost
                print(f'This is your ${change} change.')
                print()
                collected_money = self.money
                print(f"Here's your {ordered_juice}! Enjoy")
                print()
                print(f"Money in the machine is ${collected_money} .")
                print()
            
            elif inputed_amount == str or inputed_amount == float:
                print('No valid amount inputed')
                raise ValueError
    
            elif inputed_amount < cost:
                print('Your money is not sufficient for this juice')
                print(f'your ${inputed_amount} is being refunded')
    
    def make_pineapple_juice(self, ordered_juice):
        if ordered_juice not in self.ingredients_for_juice:
            print("We dont have the ordered juice")
            return False
        
        ingredients_needed = self.ingredients_for_juice[ordered_juice]['ingredients']
        cost = self.ingredients_for_juice[ordered_juice]['cost']
        
        enough_ingredients = True
        for ingredients, amount in ingredients_needed.items():
            if getattr(self, f'{ingredients}_level') < amount:
                enough_ingredients = False
                print(f"Not enough {ingredients} to make {ordered_juice} ")
                return False
        
        if enough_ingredients:
            print('please insert the required money')
            inputed_amount = int(input())
            print(f"making {ordered_juice}...")
            for ingredients, amount in ingredients_needed.items():
                setattr(self, f"{ingredients}_level", getattr(self, f"{ingredients}_level")- amount)
            self.money += cost
            
            if inputed_amount >= cost:
                change = inputed_amount - cost
                print(f'This is your ${change} change.')
                print()
                collected_money = self.money
                print(f"Here's your {ordered_juice}! Enjoy")
                print()
                print(f"Money in the machine is ${collected_money} .")
                print()
            
            elif inputed_amount == str or inputed_amount == float:
                print('No valid amount inputed')
                raise ValueError
            
            elif inputed_amount < cost:
                print('Your money is not sufficient for this juice')
                print(f'your ${inputed_amount} is being refunded')
                
    def make_lemon_juice(self, ordered_juice):
        if ordered_juice not in self.ingredients_for_juice:
            print("We dont have the ordered juice")
            return False
        
        ingredients_needed = self.ingredients_for_juice[ordered_juice]['ingredients']
        cost = self.ingredients_for_juice[ordered_juice]['cost']
        
        enough_ingredients = True
        for ingredients, amount in ingredients_needed.items():
            if getattr(self, f'{ingredients}_level') < amount:
                enough_ingredients = False
                print(f"Not enough {ingredients} to make {ordered_juice} ")
                return False
        
        if enough_ingredients:
            print('please insert the required money')
            inputed_amount = int(input())
            print(f"making {ordered_juice}...")
            for ingredients, amount in ingredients_needed.items():
                setattr(self, f"{ingredients}_level", getattr(self, f"{ingredients}_level")- amount)
            self.money += cost
            
            if inputed_amount >= cost:
                change = inputed_amount - cost
                print(f'This is your ${change} change.')
                print()
                collected_money = self.money
                print(f"Here's your {ordered_juice}! Enjoy")
                print()
                print(f"Money in the machine is ${collected_money} .")
                print()
            
            elif inputed_amount == str or inputed_amount == float:
                print('No valid amount inputed')
                raise ValueError
            
            elif inputed_amount < self.cost:
                print('Your money is not sufficient for this juice')
                print(f'your ${inputed_amount} is being refunded')
    
    def make_apple_juice(self, ordered_juice):
        if ordered_juice not in self.ingredients_for_juice:
            print("We dont have the ordered juice")
            return False
        
        ingredients_needed = self.ingredients_for_juice[ordered_juice]['ingredients']
        cost = self.ingredients_for_juice[ordered_juice]['cost']
        
        enough_ingredients = True
        for ingredients, amount in ingredients_needed.items():
            if getattr(self, f'{ingredients}_level') < amount:
                enough_ingredients = False
                print(f"Not enough {ingredients} to make {ordered_juice} ")
                return False
        
        if enough_ingredients:
            print('please insert the required money')
            inputed_amount = int(input())
            print(f"making {ordered_juice}...")
            for ingredients, amount in ingredients_needed.items():
                setattr(self, f"{ingredients}_level", getattr(self, f"{ingredients}_level")- amount)
            self.money += cost
            
            if inputed_amount >= cost:
                change = inputed_amount - cost
                print(f'This is your ${change} change.')
                print()
                collected_money = self.money
                print(f"Here's your {ordered_juice}! Enjoy")
                print()
                print(f"Money in the machine is ${collected_money} .")
                print()
            
            elif inputed_amount == str or inputed_amount == float:
                print('No valid amount inputed')
                raise ValueError
            
            
            elif inputed_amount < cost:
                print('Your money is not sufficient for this juice')
                print(f'your ${inputed_amount} is being refunded')
    
    def get_choice(self):
        self.name_of_juice = input('what would you like to have? (orange juice/banana juice/pineapple juice/lemon juice/apple juice): ')
        
    def refill_water(self, amount):
        self.water_level += amount
        print(f"Water refilled by {amount} ml. Current level: {self.water_level} ml.")
        
    def refill_ice(self, amount):
        self.ice_level += amount
        print(f"Ice refilled by {amount} ml. Current level: {self.ice_level}g.")
        
    def refill_milk(self, amount):
        self.milk_level += amount
        print(f"Milk refilled by {amount} ml. Current level: {self.milk_level} ml.")
        
    def refill_sugar(self, amount):
        self.sugar_level += amount
        print(f"Sugar added by {amount}. Current Number: {self.sugar_level}.")
        
    def refill_numOfOrange(self, amount):
        self.orange_level += amount
        print(f"Orange added by {amount}. Current Number: {self.orange_level}.")
        
    def refill_numOfBanana(self, amount):
        self.banana_level += amount
        print(f"Banana added by {amount}. Current Number: {self.banana_level}.")
        
    def refill_numOfPineapple(self, amount):
        self.pineapple_level += amount
        print(f"Pineapple added by {amount}. Current Number: {self.pineapple_level}.")
        
    def refill_numOfLemon(self, amount):
        self.lemon_level += amount
        print(f"Lemon added by {amount}. Current Number: {self.lemon_level}.")
        
    def refill_numOfApple(self, amount):
        self.apple_level += amount
        print(f"Apple added by {amount}. Current Number: {self.apple_level}.")

        





    


        
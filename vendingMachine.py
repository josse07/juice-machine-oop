class VendingMachine():
    def __init__(self, num_of_soda, num_of_candy, num_of_chips):
        self.num_of_soda = num_of_soda
        self.num_of_candy = num_of_candy
        self.num_of_chips = num_of_chips
        self.avai_operation = ['Soda', 'Candy', 'Chips', 'Report', 'off', 'ShotDown']
        self.balance = 0
    
    def soda(self, item, amount):
        type1 = {'pepsi':{'cost':200}}
        type2 = {'coca cola':{'cost':300}}
        type3 = {'7up':{'cost':150}}       
            
        if item in type1:
            cost = type1['pepsi']['cost']
            if amount >= cost:
                change = amount - cost
                print(f"Your change is ${change}")
            self.balance += cost
            print(f"Money in machine is ${self.balance}")
            print("Dispensing!!!")
            print("Here is your Pepsi, Enjoy!!!")
        
        elif item in type2:
            cost = type2['coca cola']['cost']
            if amount >= cost:
                change = amount - cost
                print(f"Your change is ${change}")
            self.balance += cost
            print(f"Money in machine is ${self.balance}")
            print("Dispensing")
            print("Here is Your Coca cola, Enjoy!!!")
            
        elif item in type3:
            cost = type3['7up']['cost']
            if amount >= cost:
                change = amount - cost
                print(f"Your change is ${change}")
            self.balance += cost
            print(f"Money in machine is ${self.balance}")
            print("Dispensing!!!")
            print("Here is your 7up, Enjoy!!!")
            
            
        else:
            print("Don't have this item")
            
    def candy(self, item, amount):
        type1 = {'sweets':{'cost':20}}
        type2 = {'snacks':{'cost':10}}
        type3 = {'chocolates':{'cost':80}}
        if item in type1:
            cost = type1['sweets']['cost']
            if amount >= cost:
                change = amount - cost
                print(f"Your change is ${change}")
            self.balance += cost
            print(f"Money in machine is ${self.balance}")
            print("Dispensing!!!")
            print("Here is your sweet, Enjoy!!!")
        
        elif item in type2:
            cost = type2['snacks']['cost']
            if amount >= cost:
                change = amount - cost
                print(f"Your change is ${change}")
            self.balance += cost
            print(f"Money in machine is ${self.balance}")
            print("Dispensing!!!")
            print("Here is your snack, Enjoy!!!")
            
        elif item in type3:
            cost = type3['chocolates']['cost']
            if amount >= cost:
                change = amount - cost
                print(f"Your change is ${change}")
            self.balance += cost
            print(f"Money in machine is ${self.balance}")
            print("Dispensing!!!")
            print("Here is your chocolate, Enjoy!!!")
            
            
        else:
            print("Don't have this item")
            
    def chips(self, item, amount):
        type1 = {'hummer chips':{'cost':100}}
        type2 = {'plantain chips':{'cost':200}}
        type3 = {'potato chips':{'cost':150}}
        
        if item in type1:
            cost = type1['hummer chips']['cost']
            if amount >= cost:
                change = amount - cost
                print(f"Your change is ${change}")
            self.balance += cost
            print(f"Money in machine is ${self.balance}")
            print("Dispensing!!!")
            print("Here is your Hummer chip, Enjoy!!!")
        
        elif item in type2:
            cost = type2['plantain chips']['cost']
            if amount >= cost:
                change = amount - cost
                print(f"Your change is ${change}")
            self.balance += cost
            print(f"Money in machine is ${self.balance}")
            print("Dispensing")
            print("Here is Your Plantain chip, Enjoy!!!")
            
        elif item in type3:
            cost = type3['potato chips']['cost']
            if amount >= cost:
                change = amount - cost
                print(f"Your change is ${change}")
            self.balance += cost
            print(f"Money in machine is ${self.balance}")
            print("Dispensing!!!")
            print("Here is your Potato chip, Enjoy!!!")
            
        
        else:
            print("Don't have this item")
    
    def choice(self, item):
        if item in self.avai_operation:
            return item  
    
    def refill_num_of_soda(self, amount):
        self.num_of_soda += amount
        print(f"Soda refilled by {amount}")
        
    def refill_num_of_candy(self, amount):
        self.num_of_candy += amount
        print(f"Candy refilled by {amount}")
    
    def refill_num_of_chips(self, amount):
        self.num_of_chips += amount
        print(f"chips refilled by {amount}")
        
        
#oVendingMachine = VendingMachine(20,50,80)
#oVendingMachine.chips('Plantain chips', 300)
#print(oVendingMachine.num_of_chips)



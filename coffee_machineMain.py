

from coffee_machinOOP import *
oCoffee_machine = Coffee_Machine(1000, 800, 500, 400)
#oCoffee = Coffee()
power = print('Power On!!!')
isNotOff = True

while isNotOff:
    print('Hello!!!')
    print()
    oCoffee_machine.get_choice()
    choice = oCoffee_machine.name_of_coffee

    if choice == 'off':
         isNotOff = False
         while isNotOff == False:
            if oCoffee_machine.water_level <= 100:
                refill_water = oCoffee_machine.refill_water(int(input('please enter amount of water ')))
                
            elif oCoffee_machine.milk_level <= 200:
                refill_milk = oCoffee_machine.refill_milk(int(input('please enter amount of milk ')))
                
            elif oCoffee_machine.sugar_level < 40:
                refill_sugar = oCoffee_machine.refill_sugar(int(input('please enter amount of sugar ')))
                
            elif oCoffee_machine.coffee_bean_level < 40:
                refill_coffee_bean = oCoffee_machine.refill_coffee_beans(int(input('please enter amount of coffee beans ')))
                
            print('GoodBye!!!')
            print()
            break
        
    elif choice == 'report':
        print(f"Water = {oCoffee_machine.water_level}ml")
        print(f"Milk = {oCoffee_machine.milk_level}ml")
        print(f"Sugar = {oCoffee_machine.sugar_level}g")
        print(f"Coffee bean = {oCoffee_machine.coffee_bean_level}g")
    
    elif choice not in oCoffee_machine.avail_coffee:
        print('dose not recongnize this coffee type')
    
    else:
        menu = oCoffee_machine.ingredients_for_coffeeType[choice]
        print(menu)
        oCoffee_machine.make_coffee(choice)
    if oCoffee_machine.water_level <= 200:
        oCoffee_machine.refill_water(int(input('please enter amount of Water ')))
    elif oCoffee_machine.milk_level <= 200:
        oCoffee_machine.refill_milk(int(input('please enter amount of Milk ')))
    elif oCoffee_machine.sugar_level <= 40:
        oCoffee_machine.refill_sugar(int(input('please enter amount of Sugar ')))
    elif oCoffee_machine.coffee_bean_level <= 40:
        oCoffee_machine.refill_coffee_beans(int(input('please enter amount of Coffee bean ')))

        
                

            
        

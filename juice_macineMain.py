from juice_machine import *
oJuice_maker = FruitJuice_machine(500, 50, 600, 100, 30, 30, 30, 30, 30)
power = input('>>> ')
print(f'Turning {power}!!!')
while power == 'On':
    User_name = 'Josse'
    password = 'josse@25'
    check_user = input('please enter your user name>>> ')
    print()
    check_password = input('please enter the user password>>> ')
    if User_name == check_user and password == check_password:
        print()
        print(f'Good day {User_name} sir how are you doing today')
        break  
    else:
        print()
        print('wrong User name Or password. please try again')

isNotOff = True
while isNotOff:
    print()
    print('To make orange juice, Press orange juice')
    print('To make banana juice, Press banana juice')
    print('To make pineapple juice, Press pineapple juice')
    print('To make lemon juice, Press lemon juice')
    print('To make apple juice, Press apple juice')
    print('To Turn Off machine, Press OFF')
    print('To show all information, Press report')
    print()
    
    oJuice_maker.get_choice()
    choice = oJuice_maker.name_of_juice
    
    choice = choice.lower()
    #choice = choice[0]# grab the first letter
    print()
    
    if choice == 'off':
        isNotOff = False
        while isNotOff == False:
            if oJuice_maker.water_level <= 100:
                refill_water = oJuice_maker.refill_water(int(input('please enter amount of water ')))
                
            elif oJuice_maker.milk_level <= 100:
                refill_milk = oJuice_maker.refill_milk(int(input('please enter amount of milk ')))
                
            elif oJuice_maker.sugar_level < 10:
                refill_sugar = oJuice_maker.refill_sugar(int(input('please enter amount of sugar ')))
                
            elif oJuice_maker.ice_level < 10:
                refill_ice = oJuice_maker.refill_ice(int(input('please enter amount of ice ')))
            
            elif oJuice_maker.orange_level < 10:
                refill_orange = oJuice_maker.refill_numOfOrange(int(input('please enter amount of orange ')))
            
            elif oJuice_maker.banana_level < 10:
                refill_banana = oJuice_maker.refill_numOfBanana(int(input('please enter amount of banana ')))
            
            elif oJuice_maker.pineapple_level < 10:
                refill_pineapple = oJuice_maker.refill_numOfPineapple(int(input('please enter amount of pineapple ')))
            
            elif oJuice_maker.lemon_level < 10:
                refill_lemon = oJuice_maker.refill_numOfLemon(int(input('please enter amount of lemon ')))
            
            elif oJuice_maker.apple_level < 10:
                refill_apple = oJuice_maker.refill_numOfApple(int(input('please enter amount of apple ')))
                
            print('Good Bye!!!')
            print()
            break
    
    elif choice == 'report':
        print(f"Water = {oJuice_maker.water_level}ml")
        print(f"Milk = {oJuice_maker.milk_level}ml")
        print(f'Ice = {oJuice_maker.ice_level}g.')
        print(f"Number of Sugar = {oJuice_maker.sugar_level}g.")
        print(f"Number of Oranges = {oJuice_maker.orange_level}g.")
        print(f"Number of Bananas = {oJuice_maker.banana_level}g.")
        print(f"Number of Pineapples = {oJuice_maker.pineapple_level}g.")
        print(f"Number of Lemons = {oJuice_maker.lemon_level}g.")
        print(f"Number of Apples = {oJuice_maker.apple_level}g.")
        print()

    elif choice not in oJuice_maker.avail_juice:
        print("We do not have this choice of juice")
    
    else:
        Menu = oJuice_maker.ingredients_for_juice[choice]
        print(Menu)
    
        if choice == 'orange juice':
            oJuice_maker.make_orange_juice(choice)
        elif choice == 'banana juice':
            oJuice_maker.make_banana_juice(choice)
        elif choice == 'pineapple juice':
            oJuice_maker.make_pineapple_juice(choice)
        elif choice == 'lemon juice':
            oJuice_maker.make_lemon_juice(choice)
        elif choice == 'apple juice':
            oJuice_maker.make_apple_juice(choice)
            
    if oJuice_maker.water_level <= 50:
        oJuice_maker.refill_water(int(input('please enter the amount of water your want to add ')))
    elif oJuice_maker.ice_level <= 10:
        oJuice_maker.refill_ice(int(input('please enter the amount of ice your want to add ')))
    elif oJuice_maker.milk_level <= 50:
        oJuice_maker.refill_milk(int(input('please enter the amount of milk your want to add ')))
    elif oJuice_maker.sugar_level <= 10:
        oJuice_maker.refill_sugar(int(input('please enter the amount of sugar your want to add ')))
    elif oJuice_maker.orange_level <= 5:
        oJuice_maker.refill_numOfOrange(int(input('please enter the amount of orange your want to add ')))
    elif oJuice_maker.banana_level <= 5:
        oJuice_maker.refill_numOfBanana(int(input('please enter the amount of banana your want to add ')))
    elif oJuice_maker.pineapple_level <= 5:
        oJuice_maker.refill_numOfPineapple(int(input('please enter the amount of pineapple your want to add ')))
    elif oJuice_maker.lemon_level <= 5:
        oJuice_maker.refill_numOfLemon(int(input('please enter the amount of lemon your want to add ')))
    elif oJuice_maker.apple_level <= 5:
        oJuice_maker.refill_numOfApple(int(input('please enter the amount of apple your want to add ')))
        
        
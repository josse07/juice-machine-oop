from vendingMachine import *
oVendingMachine = VendingMachine(30, 60, 60)
isOn = True

while isOn :
    print()
    print("To despense Soda Press Soda.")
    print("To despense Candy Press Candy.")
    print("To despense Chips Press Chips.")
    print()
    
    list_of_item_and_price = {
        'Soda':{
            'pepsi': 200,
            'coca cola': 300,
            '7up': 150
        },
        'Candy':{
            'sweets': 20,
            'snacks': 30,
            'chocolats': 80
        },
        'Chips':{
            'hummer chips': 100,
            'plantain chips': 200,
            'potato chips': 150
        }
    }
    
    print(list_of_item_and_price)
    
    print("What would you like to have")
    print()
    choice = oVendingMachine.choice(input('>>>> '))
    
    
    if choice == 'Soda':
        oVendingMachine.soda(input(''), int(input()))
        oVendingMachine.num_of_soda -= 1
    elif choice == 'Candy':
        oVendingMachine.candy(input(''), int(input()))
        oVendingMachine.num_of_candy -= 1
    elif choice == 'Chips':
        oVendingMachine.chips(input(''), int(input()))
        oVendingMachine.num_of_chips -= 1
    
    elif choice == 'Report':
        print(f"Here is the amount of {oVendingMachine.num_of_soda}")
        print(f"Here is the amount of {oVendingMachine.num_of_candy}")
        print(f"Here is the amount of {oVendingMachine.num_of_chips}")
    
    elif choice == 'ShotDown':
        print("shoting down VendingMachine")
        print('..................................')
        print()
        break

    if choice == 'off':
        while isOn == False:
            if oVendingMachine.num_of_soda < 10:
                oVendingMachine.refill_num_of_soda(int(input("Enter amount of Soda. >>> ")))
            elif oVendingMachine.num_of_candy < 10:
                oVendingMachine.refill_num_of_candy(int(input("Enter amount of Candy. >>> ")))
            elif oVendingMachine.num_of_chips < 10:
                oVendingMachine.refill_num_of_chips(int(input("Enter amount of Chips. >>> ")))
            print('Rebooting')
            print()
            break
        
    
    
    

    
    
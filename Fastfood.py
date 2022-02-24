def computation(Kain,Inom):
    totalcom = Kain + Inom
    print(totalcom)

def ChooseBurger(drink):
    burger = int(input('1 - Regular\n2 - tlc\nChoose Burger: '))
    
    if burger == 1 and drink == 1:
        computation(burger_reg,softdrinks)
    elif burger == 2 and drink == 1:
            computation(burger_tlc,softdrinks)
    elif burger == 1 and drink == 2:
            computation(burger_reg,iced_tea)
    elif burger == 2 and drink == 2:
            computation(burger_tlc,iced_tea)
    else:
        print('INVALID')

spag = 50
chicken = 75
softdrinks = 30
iced_tea = 25
burger_reg = 25
burger_tlc = 35

meal = int(input('1 - Spaghetti\n2 - Chicken\n3 - Burger\nChoose your meal: '))
drink = int(input('1 - softdrink\n2 - Iced Tea\nChoose your drink: '))

if meal == 1 and drink == 1:
    computation(spag,softdrinks)
elif meal == 1 and drink == 2:
    computation(spag,iced_tea)
elif meal == 2 and drink == 1:
    computation(chicken,softdrinks)
elif meal == 2 and drink == 2:
    computation(chicken,iced_tea)
elif meal == 3 and drink == 1:
    ChooseBurger(drink)
elif meal == 3 and drink == 2:
    ChooseBurger(drink)
else:
    print('INVALID')
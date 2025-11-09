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
def update_resoures(coffee_type):
    '''update global resouce data '''
    used_resources = MENU[coffee_type]['ingredients']
    global resource
    for key in used_resources:
        resources[key] = resources[key]-used_resources[key]

def is_enough_resources(coffee_type):
    '''check resouces for particular coffee type'''
    global resources
    required_ingreds = MENU[coffee_type]['ingredients']
    for key in required_ingreds:
        if resources[key] - required_ingreds[key] < 0:
            return False
    return True

def take_money_from_user():
    '''take money from user and return total money given by the user'''
    quaters_count = int(input('enter the num of quaters: '))
    dimes_count = int(input('enter the num of dimes: '))
    nickles_count = int(input('enter the num of nickle: '))
    pennies_count = int(input('enter the num of pennies: '))
    given_money = quaters_count*.25 + dimes_count*.10 + nickles_count*.05 + pennies_count*.01

    return given_money
while True:
    user_input = input('What would you like? (espresso/latte/cappuccino): ').lower()

    if user_input=='report':
        for key in resources:
            print(key,resources[key])
        continue
    if user_input=='espresso' or user_input == 'latte' or user_input =='cappuccino':
        isEnough = is_enough_resources(user_input)
        if not isEnough:
            print('we dont have enough resouces for this coffee!!!')
            print('give it another try')
            continue
        sell_price = MENU[user_input]['cost']
        given_money = take_money_from_user()
        if given_money-sell_price < 0:
            print('not enough money')
            continue

        print('total changed amount would be: ', round(given_money-sell_price,2))
        update_resoures(user_input)
        print('here is your coffee sir !!! ')
        print('ty for visiting please come again !!!')
        continue

    else:
        print('invalid input please try again !!!')
        continue
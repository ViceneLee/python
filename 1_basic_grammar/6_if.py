"""
    if
"""
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

"""
    判断==
"""
age = 18
print(age == 18)

"""
    判断!=
"""
answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")

age_0 = 22
age_1 = 18

"""
    and
"""
print(age_0 >= 21 and age_1 >= 21)

"""
    or
"""
print(age_0 >= 21 or age_1 >= 21)

"""
    判断in
"""
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)

"""
    判断not in
"""
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

"""
    if elseif else
"""
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")

"""
    if
"""
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
    print("\nFinished making your pizza!")

"""
    for if
"""
available_toppings = ['mushrooms', 'olives', 'green peppers',
 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
        print("\nFinished making your pizza!")
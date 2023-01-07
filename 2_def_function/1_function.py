"""
    方法
"""
def greet_user():
    """显示简单的问候语。"""
    print("Hello!")
greet_user()

"""
    带参方法
"""
def greet_user(username):
    print(f"Hello, {username.title()}!")
greet_user('jesse')

"""
    带参方法
"""
def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type}.")

    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('hamster', 'harry')

"""
    带参方法(关键字实参)
"""
describe_pet(animal_type='hamster', pet_name='harry')

"""
    默认值
"""
def describe_pet(pet_name, animal_type='dog'):
 """显示宠物的信息。"""
 print(f"\nI have a {animal_type}.")
 print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet(pet_name='willie')

def describe_pet(pet_name, animal_type='dog'):
    print(f"\nI have a {animal_type}.")

"""
    等效调用
"""
describe_pet('willie')
describe_pet(pet_name='willie')
# 一只名为Harry的仓鼠。
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')

"""
    返回值
"""
def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)

"""
    返回对象
"""
def build_person(first_name, last_name):
    person = {'first': first_name, 'last': last_name}
    return person
musician = build_person('jimi', 'hendrix')
print(musician)

def greet_users(names):
    """向列表中的每位用户发出简单的问候。"""
    for name in names:
        msg = f"Hello, {name.title()}!"
    print(msg)
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

# 首先创建一个列表，其中包含一些要打印的设计。
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
# 模拟打印每个设计，直到没有未打印的设计为止。
# 打印每个设计后，都将其移到列表completed_models中。
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

# 显示打印好的所有模型。
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

"""
    形参名*toppings 中的星号让Python创建一个名为toppings 的空元组，并将收
    到的所有值都封装到这个元组中。
"""
def make_pizza(*toppings):
    """打印顾客点的所有配料。"""
    print(toppings)
make_pizza('mushrooms', 'green peppers', 'extra cheese')


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

"""
    函数接受不同类型的实参，必须在函数定义中将接纳任意数量实参的形参放在最后
"""
def make_pizza(size, *toppings):
    """概述要制作的比萨。"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

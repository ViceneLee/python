"""
    列表
"""
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())

message = f"My first bicycle was a {bicycles[0].title()}."
print(message)

"""
    列表后添加
"""
bicycles.append('ducati')
print(bicycles)

"""
    在某个位置添加元素
"""
bicycles.insert(0, 'ducati1')
print(bicycles)

"""
    删除元素
"""
del bicycles[1]

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

"""
    弹出最后一个元素
"""
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

"""
    弹出某个位置的元素
"""
first_owned = motorcycles.pop(1)

"""
    删除元素
"""
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')

"""
    排序
"""
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

"""
    反转
"""
cars.sort(reverse=True)
print(cars)

"""
    正排
"""
print(sorted(cars))

"""
    反转
"""
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(cars)

"""
    长度
"""
len(cars)
"""
    0,1,2
"""
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

"""
    1,2,3
"""
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4])

"""
    0,1,2,3
"""
print(players[:4])

"""
    2 ->
"""
print(players[2:])

"""
    'charles', 'martina', 'michael', 'florence', 'eli'
        0           1         2           3        4
        -4         -3        -2          -1        0
"""
print(players[-3:])

for player in players[:3]:
    print(player.title())

"""
    复制数组
"""
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
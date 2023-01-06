"""
    遍历
"""
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

"""
    遍历+方法
"""
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

"""
    数字遍历  [1,5)
"""
for value in range(1, 5):
    print(value)

"""
    函数range() 从2开始数，然后不断加2，直到达到或超过终值（11）
"""
for value in range(2, 11, 2):
    print(value)

"""
    平方
"""
squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)

"""
    平方
"""
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

squares = [value**2 for value in range(1, 11)]
print(squares)


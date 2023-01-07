"""
    读取文件
"""
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)

"""
    绝对路径
"""
with open('/Users/vicene/program/backend/python/workspace/python/3_exception_file/pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)

"""
    读取每行
"""
with open('/Users/vicene/program/backend/python/workspace/python/3_exception_file/pi_digits.txt') as file_object:
    for line in file_object:
        print(line)

"""
    读取每行
"""
with open('/Users/vicene/program/backend/python/workspace/python/3_exception_file/pi_digits.txt') as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())

"""
    写入
"""
filename = 'pi_digits.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.")
    file_object.write("I love creating new games.\n")


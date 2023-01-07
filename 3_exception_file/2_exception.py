"""
    异常处理
"""
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
        second_number = input("Second number: ")
    if second_number == 'q':
        break
    answer = int(first_number) / int(second_number)
    print(answer)

"""
    非异常后读取文件
"""
def count_words(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")
filename = 'alice.txt'
count_words(filename)


"""
    静默
"""
def count_words(filename):
    try:
        a = 1+1
    except FileNotFoundError:
        pass
    else:
        pass
filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt','little_women.txt']
for filename in filenames:
    count_words(filename)
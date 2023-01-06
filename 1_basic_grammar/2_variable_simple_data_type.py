name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

"""
    字符串的变量
"""
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)

"""
    创建消息，再把整条消息赋给变量
"""
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message)

full_name = "{} {}".format(first_name, last_name)
print(full_name)


"""
    制表符或换行符
    \t  制表符
    \n  换行符
    
"""
print("\tPython")
print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavaScript")

"""
    删除空白
"""
favorite_language = 'python '
print(favorite_language.rstrip())




# A variable is used to store data that may change during program execution.

name = input("Enter user name:")
print(f"type of data name is {type(name)}")
print(f"User name is :{name}")

# memory location of a variable : id()--function use 
print(f"memory location of name varaible :{id(name)}")
a=10
print(f"location of a in memory:{id(a)}")


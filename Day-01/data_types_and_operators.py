# Data type tells what kind of data is stored in a variable: int, float, string

# int : Used for whole numbers (no decimal).
# a= 12
# print(f"which type of a data type:{a}:{type(a)}")

# float: Used for decimal numbers.
# price = 33.11
# print(f"which type of a data type:{price}"\n"{type(price)}") # error : " \n" \n is outside the string → Python gets confused.
# print(f"which type of a data type:{price}\n{type(price)}") 

# string: Used for text (written inside quotes) " "(double quotes) or ' '(single quotes)
# name="Suraj"
# print(f"your name is:{name}\nwhich type of name data type:{type(name)}") 

# name1='Suraj'
# print(name1)

# operator in pyton:Operators are symbols used to perform operations on values or variables.
# 1: Arithmetic Operators: Used to perform mathematical calculations.
'''
a=float(input("Enter first number:"))
b=float(input("Enter second number:"))

print(f"sum of two numbers:{a+b}")
print(f"subraction of two numbers:{a-b}")
print(f"multiplication of two numbers:{a*b}")
print(f"division of two numbers:{a/b}")  
print(f"modulus of two numbers:{a%b}")
print(f"power  of a:{a**b}")
print(f"floor division numbers:{a//b}")
'''

# 2: Assignment Operators:Used to assign values to variables.
# a=10
# a+=5
# print(f"a is assign :{a}")

# 3: Comparison (Relational) Operators: Used to compare two values -->> Result is always True or False.
'''
a=float(input("Enter first number:"))
b=float(input("Enter second number:"))

print(f"equal operator:{a==b}")
print(f"a:{a} is not equal to b:{b} :{a!=b} ")
print(f"greater than operator:{a>b}")
print(f"less than operator:{a<b}")
print(f"greater than equal operator:{a>=b}")
print(f"less than equal operator:{a<=b}")
'''
# 4: Logical Operators: and, or, not
# a=float(input("Enter first number:"))
# b=float(input("Enter second number:"))

# # print(f"a and b is:{a > b and b <a}")
# # print(f"a or b is:{a >b or b>a}")

# print(f"a is greater than b: {not(a >b)}")

# 5️: Identity Operators: Used to check whether two variables refer to the same object in memory: is(same object)-->True and is not(different obj):False
# a=int(input("enter a first number:"))
# b=int(input("enter a second number:"))
# print(f"memory location of a is:{id(a)}:{a is b}")
# print(f"memory location of b is:{id(b)}:{a is not b}")

# 6️⃣ Membership Operators: Used to check whether a value exists in a sequence (list, string, tuple): in(value exits) and not in(value does not exists
# list1=[2,4,6,8,10]
# # print(f"2 is present in list1:{2 in list1}") # True
# print(f"10 is present in list1:{10 in list1}") # True
# print(f"10 is  present in list1:{10 not in list1}") # False

name='Suraj'
print(f"S in present name:{'S' in name}")
print(f"s in present name:{'s' in name}")
print(f"u in present name:{'u' in name}")
print(f"R in present name:{'R' in name}")
print(f"j in present name:{'j' in name}")
print(f"Q in present name:{'Q' in name}")
print(f"j in present name:{'j' not in name}")
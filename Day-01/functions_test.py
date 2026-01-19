# SCRIPTING :SET OF INSTRUCTION 
# functions: 

def sum_of_num(): # function define
    num1 = int(input("enter first number:"))
    num2 = int(input("enter second number:"))

    sum = num1+num2
    print(f"sum of two number:{sum}")

# sum_of_num() # function calling
env = input("Enter the Environment:") # taking input from user 
print(f"The user Environment is {env}.") 

if env == "prd":
    sum_of_num()
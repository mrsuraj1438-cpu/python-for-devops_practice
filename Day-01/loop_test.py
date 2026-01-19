# # get the 10 user input

# for i in range(10):

#     env = input("Enter the Environment:")

#     if env == "prd":
#         print("Don't Deploy on Friday")

#     elif env == "stg":
#         print("take backup and test well")
        
#     else:
#         print("Safe to deploy any day")    

# print the table using loop:
# num = int(input("Enter the number you want the table:"))

# for i in range(1,11):
#     print(f"{num} x {i} = {num * i}")

# while loop:when condition is true loop is continuous work if condition is false loop stop 

# i = 1

# while i <=6:
#     print(i)
#     i +=1
# age = int(input("enter your age:"))

# if age !=18:
#     print("age is not 18")
# else:
#     print("age is 18")    

# while age !=18:
#     print("hello")
#     break

choice =input("enter your choice(press q to quit):")

while choice !="q":
    num = int(input("Enter the number you want the table:"))
    # choice =input("enter your choice(press q to quit):")
    for i in range(1,11):
        print(f"{num} x {i} = {num * i}")
    choice =input("enter your choice(press q to quit):")


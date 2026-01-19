# get the environment from user and print it

# env =input("Enter the Environment:").title()
env = input("Enter the Environment:")
# print(f"The user Environment is {env}.")

if env == "prd":
    print("Don't Deploy on Friday")

elif env == "stg":
    print("take backup and test well")
    
else:
    print("Safe to deploy any day")    
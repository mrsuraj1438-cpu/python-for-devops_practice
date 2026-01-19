# without exception handling the proram is crash
'''
num = int(input("enter a number:"))

divide = num/0

print(divide)
'''
# when we use the exception handling it is prevent to not crash the program

try:
    # num = int(input("enter a number:"))
    # divide = 10/num
    # print(f"{divide:.2f}")
    # list = ["Hello\n", "This is line 2\n"]
    txt = input("enter only number you want:")
    # txt = int(input("enter only number you want:"))
    with open("file.txt", "a") as file:
        file.write(txt + '\n')
   
    print("Lines written successfully")  
# except ZeroDivisionError:
#     print("cannot divide by zero")
    
# except ValueError:
#     print("enter only number")    

except Exception as e:
    print("which type of error is found:",type(e))

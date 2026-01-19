import psutil
# function:A function is a reusable block of code that performs one specific task.

# def greet():
#     print("Happy New Year brother @@@@")

# greet()

# function with arguments(parameters)
# def name(name): # inside--> name(this is parameter1, parameter2):
#     print(f"Hello,{name}")

# name("Suraj") # name("suraj" --> this is arguments)
# name("Pooja")

# def multiply(a,b):
#     print(f"multiplication of two number:{a * b}")

# multiply(12,2)

# def add(a,b):
#     return a + b

# print(add(12,2))
# print(add(12,22))

# cpu usage check 

def cpu_usage():

    thres_hold=int(input("Enter the threshold:"))
    print(f"The threshold is:{thres_hold} ")

    current_usage=psutil.cpu_percent(interval=1)
    print(f"current CPU usage is:{current_usage}%")

    if current_usage > thres_hold:
        print("CPU usage is maximum to threshold")

    else:
        print("CPU usage is good ")

cpu_usage()
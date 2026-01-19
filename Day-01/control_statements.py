# control statements: control the flow a program
# Python has 3 main types:
# 1: Decision-making statements: if statement-->Executes a block of code only if the condition is true.
# age=int(input("enter your age:"))

# if age >=18:
#     print("You are eligible for driving license!!!")
# else:
#     print("you are under age not eligible for driving license!!!")

# if-elif-else
'''
marks=int(input("Enter your subject1 marks:"))

if marks>=90:
    print("Grade A")

elif marks>=80:
    print("Grade B")   

elif marks>=70:
    print("Grade C")

else:
    print("Don't give up and keep hardworking")
'''

# print given number is even or not
# num=int(input("enter your number:"))

# if num %2==0:
#     print(f"given number is even:{num}")

# else:
#     print(f"given number is not even:{num}")    


# print which number is greater in three numbers: a ,b ,c
'''
a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))

if a > b:
    if a >c:
        print("a is the greatest number")
    else:
        print("c is the greatest number")  
else:
    if b > c:
        print("b is the greatest number")
    else:
        print("c is the greatest number")
'''

# for loop:Used when we know the number of repetitions.
# i=1

# for i in range(1,21):
#     print(i)

# while loop: when condition is true loop will run forever(infinite loop) but if condition is false loop will be stop.
# i=1

# while i<10:
#     print(i)
#     i = i+1

# Jump / Control Transfer Statement:These statements change loop execution suddenly.
# A: break : used to stop the loop immediately
# i=1

# while i<10:
#     if i == 5:
#         break
#     print(i)
#     i = i+1


# for i in range(1,21):
#     if i ==5:
#         break
#     print(i)

# B: continue:Used to skip the current iteration and move to the next.
# for j in range(1, 21):
#     if j ==7:
#         continue
#     print(j)

# C: pass:pass does nothing and Used when statement is required but no code is written yet.
# for j in range(1, 21):
#     if j ==7:
#         pass
#     print(j)

# Simple calculator
'''
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
op = input("Enter operator(+,-,*,/): ")

if op == '+':
    print(f"sum of two number is:{num1+num2}")

elif op == '-':
    print(f"sub of two number is:{num1-num2}")

elif op == '*':
    print(f"multiplication of two number is:{num1*num2}")

elif op == '/':
    print(f"division of two number is:{num1/num2}")

else:
    print(f"Invalid operator:{op}")
'''

# print a table number:

num =int(input("Enter number: "))

for i in range(1,11):
    print(f"{num} X {i} = {num * i}")
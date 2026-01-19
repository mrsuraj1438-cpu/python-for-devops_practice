# create a class name Dog:
'''
class Dog:
    species = "Bulldog" # class variable anyone can access:
    
    def __init__(self, name, age):
        self.name = name  # instance varibale only name access
        self.age = age   # instance variable only age access
        
    def full_name(self):
        return f"full_details : breed is {self.species} \n dog name: {self.name} and age is {self.age}." 

# Create an object of class


dog1 = Dog("Aadi", 5)
breed = dog1.species
print(breed)
print(dog1.full_name())

# second obj
dog2 = Dog("Luccy",2)
print(dog2.full_name())
'''

# create a class user and check their status

class User:
    
    def __init__(self, username ,logged_in):
        self.username = username
        self.logged_in = logged_in
        
    def log_user(self):
        if self.logged_in:
            # return f"{self.username} is  and login successful"
            print(f"{self.username} is  and login successful")
            
        else:
            # return f"{self.username} is  and login successful"
            print(f"{self.username} is  and login successful")

            
        
    
user1 = User("Suraj", True)
user2 = User("Alex", False)

# If function uses print() inside → just call function
# If function uses return → use print(function())

# check status
user1.log_user() # --> firsr user1
user2.log_user() # -- second user2
# print(user1.log_user())
# print(user2.log_user())

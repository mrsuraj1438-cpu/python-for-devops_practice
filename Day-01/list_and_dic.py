import requests
# empty list
# a=[]
# print(f"list :{type(a)} ")


# simple list: that can store different types of data
# diff_list =["suraj",12, 33.2, True]
# print(f"different types of data store in list:{diff_list}")
# print(f"{diff_list[0]}") # retreived the 0th location data:
# print(f"{diff_list[3]}")

# server = ["app1","app2", "app3"]
# # print(f"all servers :{server}")
# print("all servers:")

# for i in server:   
#      print(i)

# print(dir(server))
# print(server.append.__doc__)
# print(server.count.__doc__)

# write the list with second method : data = list()
# cloud = list() 
# print(f"data type of cloud:{type(cloud)}")

# append the value in cloud
# cloud.append("AWS")
# cloud.append("AZURE")
# cloud.append("GCP")
# cloud.append("DIGITALOCEAN")
# cloud.append("ALIBABA")
# cloud.append("AWS")
# cloud.append("AWS")
# cloud.append("AWS")
# cloud.append("AWS")
# cloud.append("AWS")
# cloud.append("AWS")

# after data append in cloud
# print(f"cloud :{cloud}")

# access the cloud 
# print(f"which cloud 0th location: {cloud[0]}")
# print(f"which cloud 1st location: {cloud[1]}")
# print(f"which cloud 2nd location: {cloud[2]}")
# print(f"which cloud 3rd location: {cloud[3]}")
# print(f"which cloud 4th location: {cloud[4]}")

# print(f"how many times aws in cloud:{cloud.count("AWS")}")

#Remove the AWS in cloud
# for i in cloud[:]:
#     if i == "AWS":
#      cloud.remove("AWS")

# print(f"after removing AWS in cloud:{cloud}")
# cloud.sort()
# print("after sorting the cloud:",cloud)
# print(f"how many cloud service provider in the cloud:{len(cloud)}")

# print(cloud)
# # 
# # print(dir(cloud))
# # pop use: cloud.pop()
# print(cloud.pop(3))
# print(cloud)

# remove: the is use for delete the data in cloud: cloud.remove()

# cloud.remove("AWS")
# print(f"after removing the AWS in cloud:{cloud}")

# cloud =(input("enter your clouds: ").upper()) # this use for string --> suraj- "S","U","R","j"
'''
cloud =(input("enter your clouds: ").upper()).split() # this create list-- by using .split()
# for loop in use :

for clouds in cloud:
    if clouds == "AWS":
        print(f"Market leader of the clouds:{clouds}")
    elif clouds == "AZURE":
        print(f"Microsoft provide this cloud service:{clouds}")
    elif clouds == "ALIBABA":
        print(f"jake ma the founder of the this cloud:{clouds}")
    else:
        print("cloud not study !!!!!!")
'''

# dictionary data type: this store the data in key , value pair :: {}

# dic ={}
# print("Empty dictionary and type of dic:",type(dic))

# store the data in dic

# dic1 ={
#     "AWS": "Market leader",
#     "AZURE": "Microsoft cloud",
#     "GCP": "Goolge cloud"
# }
# print(f"dic1 store the clouds:{dic1}")

# add new cloud provider

# dic1["ALIBABA"] = "Jack's ma cloud"
# print(f"after adding alibaba cloud in dic1:{dic1}")

# # updating existing cloud :GCP

# dic1["GCP"] = "Pay as per use this cloud seriveces"
# print(f"after update the value of GCP cloud in dic1:{dic1}")

# delete the item in cloud use : del dic["key"]

# del dic1["AWS"]
# print("delete the AWS:",dic1)

# .pop("key") --> return the value
# removed = dic1.pop("GCP")
# print(removed)

# print(f"after pop out the GCP:{dic1}")


# for loop use in dictionary:
# for key, value in dic1.items():
#     print(f"{key}: {value}")

# loop through servers and ips

# servers = {"web01": "10.0.2.0",
#            "db01": "10.0.1.0"
# }

# for server, ip in servers.items():
#     print(f"{server}: {ip}")

# add new node01 in servers:
# servers["node01"] = "192.0.2.0"

# print(f"after add node in server:{servers}")

# # update the web01 ip address --> 198.11.0.1
# servers["web01"] = "198.11.0.1"
# print(f"after update the web01 update ip in server:{servers}")

# Duplicates Not Allowed in beacause: Dictionaries cannot have two items with the same key
'''
this_dic = {
    "Name": "Suraj",
    "Age": 24,
    "Married": False,
    "Year": 2025
}

this_dic1 = {
    "Name": "Suraj",
    "Age": 24,
    "Married": False,
    "Year": 2025,
    "Year": 2024
}

print(this_dic)
print(this_dic1)
print(f"length of the dicitionary:{(len(this_dic1))}")
'''
#Data Types: The values in dictionary items can be of any data type:

# diff_dic = {
#     "Name": "Suraj",
#     "Age": 24,
#     "Married": False,
#     "list": ["s",12, True, 12.12]
# }

# print(f"different data types in dictionary:{diff_dic}")

# how to make dictionary

# second_dic = dict(name ="Suraj", age=27, married=False, year=2025)
# print(f"second_dic:{type(second_dic)} \n{second_dic}")

# how to access the values in the dicitionary:

# x = diff_dic["Name"]
# print(x)

# print(diff_dic.get("Age")) # access the value of age : .get("key_name")

# print all keys and values
# print(f"all keys are :{diff_dic.keys()}")
# print(f"all values are :{diff_dic.values()}")

# update the dictionary

# diff_dic["Age"] = 20
# print(update_age)

# print(diff_dic)

# Get a list of the key:value pairs : using .items()
# print(diff_dic.items())

# To determine if a specified key is present in a dictionary use the in keyword:

'''

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

name =input("enter your what you want:")
if name in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
else:
  print("not in this dictionary")

'''
# update the dicitonary using update() method:
# x=thisdict.update({"model":"Bugati"})
# print(x)
# print("update the model in the dicinary:",thisdict)

# Removing Items : pop() return the value, popitem() -- give the key and value :: del dic_name["key"]
# p= thisdict.pop("model")
# p3= thisdict.popitem()
# p2= thisdict.popitem()
# p1= thisdict.popitem()
# # print(p)
# print(p3)
# print(p2)
# print(p1)

# del thisdict["year"]
# print(f"delete the year in this_dic:{thisdict}")

# delete the dicitonary

# del thisdict
# print("delete the dictionary:")
# print(thisdict)

# apply the for loop and operations

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# print all keys names:
# for i in thisdict:
#     print(i)

# # print all values names:
# for i in thisdict:
#     print(thisdict[i])

# print all keys and values using method: keys() and values()
# print("all keys are:")
# print("all values are:")
# for i in thisdict.keys():
#     print(i)

# for i in thisdict.values():
#     print(i)

# print keys and values : using items()

# for x,y in thisdict.items():
    # print(x,y)

#  Copy a Dictionary using : copy()
# my_dict = thisdict.copy()
# print(f"before copy the data original dicitonary dictionary:{thisdict}")
# print(f"all the data copy from this_dic to my_dict:{my_dict}")

# nested dictionary :A dictionary can contain dictionaries, this is called nested dictionaries.
'''
family={

    "child1": {
        "name": "Suraj",
        "age":24    
    },

    "child2": {
        "name": "Neeraj",
        "age":22
    },

    "child3": {
        "name": "Someone",
        "age": 20
    }
}
'''


product = {
    "id": "1",
    "name": "Google Pixel 6 Pro",
    "data": {
        "color": "Cloudy White",
        "capacity": "128 GB"
    }
}

# print(product["data"]["color"])

# for key, value in product.items():
#     print("",key)

#     for y in value.items():
#       print(y+ ':', value[y])
# print(f"nested dictionary that can three dic:{family}")

# access the child2: data 

# print(f"child2 name is: {family["child2"]["name"]}")
# print(f"child3 name is: {family["child3"]["name"]}")

# for loop use to print the values:

# for i,j in family.items():
#     print(i,j)

# retrieve all the child data in family dicitionary 
# for x , obj in family.items(): # x = the key (like "child1") and obj = the dictionary for that child 
#     print("",x)
    
#     for y in obj:              # y = key inside each child dictionary :so ("name" then "year")
#         print(y+ ':', obj[y])  # obj[y] = value for that key      


# data --10-01-2025  practice dic : questions:-

products = {
    "product1": {
        "name": "Apple 12pro",
        "price": 50000,
        "process": "AMz2",
        "Screen": None
    },
    "product2": {
        "name": "iPad Mini",
        "price": 419.99,
        "Screen": 4.5
    },
    "product3": {
        "name": "iPad Mini Pro",
        "price": 519.99,
        "Screen": 8.3
    }
}

# print all products
# print(products)
# print product1
# print(products["product1"]["price"])
print(product["name"])

def  api_fun():
    try:
        for x in products().items():
          print(x,":")
        #   print("specs:")
        #   if y["Screen"] is not None:
        #       for y in obj:
        #         print(y+ ':', obj[y])
        #   else:
        #      print("value not available")
        #   print("-" * 20)
    except Exception as e:
       print("Error",e)

api_fun()
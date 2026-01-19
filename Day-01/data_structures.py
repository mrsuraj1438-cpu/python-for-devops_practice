# list: 
# a = [12,232,4,"Suraj",True] # how to write list first method
# print(type(a))
# a.append(122)
# print(a)

# cloud = list() # how to write list second method
# print(type(cloud))
# cloud.append("AWS")
# cloud.append("AZURE")
# cloud.append("GCP")
# cloud.append("ORACLE")
# cloud.append("ALIBABA")
# cloud.append("DIGITAL_OCEAN")

# print(f"length of the cloud:{len(cloud)}")
# print(F"Cloud servive provider:{cloud}")
# print(f"location of AWS in clouds:{cloud[1]}")
# # print(dir(cloud))
# print(cloud.count.__doc__)
# print(cloud.sort.__doc__)
# print(cloud.remove.__doc__)
# print(f"all cloud providers:{cloud[0:6]}")
# print(cloud.count("AWS"))
# print(cloud.sort(),cloud)

# data:02-01-2026

cloud = list() # how to write list second method
print(type(cloud))
cloud.append("AWS")
cloud.append("AZURE")
cloud.append("GCP")
cloud.append("ORACLE")
cloud.append("ALIBABA")
cloud.append("DIGITAL_OCEAN")
cloud.append("Utho")
# print(cloud)

# for i in cloud:
#     print(i)

for clouds in cloud:
    if clouds == "AWS":
        print(f"{clouds}: market leader of the Cloud")
    elif clouds == "Utho":
        print(f"{clouds}: indian Cloud provider")    
    elif clouds == "DIGITAL_OCEAN":
        print(f"{clouds}: Self study to find it these clouds")
    else:
        print(f"{clouds}: these clouds not study")
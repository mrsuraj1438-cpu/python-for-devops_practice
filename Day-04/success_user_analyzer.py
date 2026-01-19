
def log_read():
    
    # read the data from file: auth.log
    with open("auth.log", "r") as log_user:
        # print(f"log_user:{log_user.readlines()}")
        return log_user.readlines()


def log_analyzer(lines):
    
    # create a dictinoary to store log_counts:
    login_user_count = {
        "SUCCESS":0,
        "FAILED":0
    }        
    
    for line in lines:
        if "SUCCESS" in line:
            login_user_count["SUCCESS"] += 1
        elif "FAILED" in line:
            login_user_count["FAILED"] += 1
        else:
            pass   
    
    return login_user_count 
def print_user(lines):
    
    user_status = input("enter successfule or failed user: ").upper()

    unique_user = set()
    # print(ask_user)
    # if user_status == "SUCCESS":
    for line in lines:
            
            
                if "SUCCESS" in line:
                    parts = line.split("User ")
                    if len(parts) > 1:
                        user_name = parts[1].split()[0]
                        unique_user.add(user_name)  
                        # print(unique_user)
                            
                elif user_status == "FAILED":
                    if "FAILED" in line:
                        parts = line.split("User ")
                        if len(parts) > 1:
                            user_name = parts[1].split()[0]
                            unique_user.add(user_name)
        
    # else:
    #     print("enter a valide name") 
    if user_status == "SUCCESS": 
        print("The SUCCESS login users :")
        for user in unique_user:
            print(user.capitalize())
            
    elif user_status == "FAILED":
        print("The FAILED login users :")
        for user in unique_user:
            print(user.capitalize())
    
    else:
        pass
    
    with open("user.txt", "w") as file:
            for user1 in unique_user:
                file.write(user1 + "\n")
    print("file is successfulyy saved!!")
    
    
    
lines = log_read()
counts = log_analyzer(lines)
print("counts are:", counts)
print_user(lines)

# save this not file:



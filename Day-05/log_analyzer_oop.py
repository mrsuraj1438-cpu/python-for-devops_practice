# create a class

class AuthLogMonitor:
    
    def __init__(self, username ):
        self.username = username
        
    def log_read(self):
        
        # read the data from file: auth.log
        with open("auth.log", "r") as log_user:
            # print(f"log_user:{log_user.readlines()}")
            return log_user.readlines()


    def log_analyzer(self, lines):
        
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
        
        
user1 = AuthLogMonitor("Suraj")
print(f"user name is: {user1.username}")
line = user1.log_read()
print(user1.log_analyzer(line))


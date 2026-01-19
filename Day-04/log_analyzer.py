# read the app.log file
log = "app.log"

# step 2: store log tyes in list
log_levels = ["INFO", "WARNING", "ERROR"]

# step3: Dictionary to store counts
log_count = {
    
}

with open("app.log", "r") as file:
    content = file.read()
    print(f"app_log:{content}")
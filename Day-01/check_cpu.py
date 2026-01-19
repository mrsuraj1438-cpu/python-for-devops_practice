# aapko kaam karna hai ki user se CPU threshold lo 
# current cpu usage pata karo 
# agar cpu usage threshold se jyda hua , email kar do
import psutil

def get_cpu_usage():
    cpu_threshold = int(input("enter the cpu threshold:"))
    print(f"cpu threshold is {cpu_threshold} %")
    current_cpu = psutil.cpu_percent(interval=1)
    print(f"current cpu usage  is {current_cpu} %")
    
    email = "cpu@gmail.com" # dummy email
    if current_cpu > cpu_threshold:
        print(f"CPU alert email sent to {email}")
    else:
        print("cpu in safe state...")    
    
    # Check RAM usage
    ram_usage = psutil.virtual_memory()
    system_ram_usage = ram_usage.percent
    one_gb =  1073741824  # bytes 
    
    # taking ram threshold from user:
    ram_threshold =int(input("enter the RAM threshold:"))
    print(f"RAM threshold is {ram_threshold} %")
    print("Check RAM usage:")
    
    # compare system ram with ram threshold
    if system_ram_usage > ram_threshold:
        print(f"ALERT for RAM USAGE:{system_ram_usage}")

    else:
        print(f"Total RAM :{ram_usage.total/one_gb:.2F} GB" )  # convert bytes into gb
        print(f"RAM used :{ram_usage.used/one_gb:.2F} GB")
        print(f"Available RAM :{ram_usage.available/one_gb:.2F} GB")
        print(f"RAM Usage :{ram_usage.percent:.2F} %")

    # Check disk usage
    disk = psutil.disk_usage('C:\\')
    system_disk_usage = disk.percent

    # taking disk threshold from user:
    disk_threshold = int(input("enter the Disk threshold:"))
    print(f"Disk threshold is {disk_threshold} %")
    print("Check Disk usage")

    # compare system_disk with disk threshold
    if system_disk_usage > disk_threshold:
        print(f"ALERT for HIGH USAGE DISK:{system_disk_usage}")
    else:
        print(f"Total Disk :{disk.total/one_gb:.2F} GB" )
        print(f"Used Disk :{disk.used/one_gb:.2F} GB")
        print(f"Free Disk :{disk.free/one_gb:.2F} GB")
        print(f"Disk Usage :{disk.percent:.2F} %")

# function call

get_cpu_usage()
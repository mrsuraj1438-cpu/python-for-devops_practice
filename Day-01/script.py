import psutil
#A Python script is a program used to automate tasks
# ->> such as monitoring, deployment, and system management in DevOps.

#why scripts use:
# DevOps work has repetitive tasks, like:
# Checking CPU usage
# Monitoring memory
# Taking backups
# Restarting servers
# Deploying applications
# Cleaning logs

# check cpu_usage:
cpu_threshold=int(input("Enter the CPU threshold:"))
print(f"CPU threshold is:{cpu_threshold}")

current_cpu=psutil.cpu_percent(interval=1)
print(f"current CPU Usage is:{current_cpu}%")

if current_cpu > cpu_threshold:
    print("⚠️  High CPU usage! Take action ")
else:
    print("CPU usage is normal. ")    
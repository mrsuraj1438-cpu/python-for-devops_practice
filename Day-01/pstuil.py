import psutil

cpu = psutil.cpu_percent(interval=1)
print("CPU Usage:", cpu, "%")

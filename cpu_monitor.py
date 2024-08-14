import psutil
import datetime

# Get CPU usage
cpu_usage = psutil.cpu_percent(interval=1)

# Get current time
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Log CPU usage to a file
with open("/home/affiliatework2016/system_health.log", "a") as log_file:
    log_file.write(f"{current_time} - CPU Usage: {cpu_usage}%\n")

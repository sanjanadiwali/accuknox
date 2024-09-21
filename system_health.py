import psutil
import logging

# Setup logging
logging.basicConfig(filename='system_health.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Thresholds
CPU_THRESHOLD = 80.0  # CPU usage in %
MEMORY_THRESHOLD = 80.0  # Memory usage in %
DISK_THRESHOLD = 90.0  # Disk usage in %
PROCESS_THRESHOLD = 300  # Max number of processes

def check_cpu():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        logging.warning(f"High CPU usage: {cpu_usage}%")
    return cpu_usage

def check_memory():
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent
    if memory_usage > MEMORY_THRESHOLD:
        logging.warning(f"High Memory usage: {memory_usage}%")
    return memory_usage

def check_disk():
    disk_usage = psutil.disk_usage('/')
    if disk_usage.percent > DISK_THRESHOLD:
        logging.warning(f"Low Disk Space: {disk_usage.percent}% used")
    return disk_usage.percent

def check_processes():
    process_count = len(psutil.pids())
    if process_count > PROCESS_THRESHOLD:
        logging.warning(f"High number of processes: {process_count}")
    return process_count

def system_health_check():
    cpu = check_cpu()
    memory = check_memory()
    disk = check_disk()
    processes = check_processes()

    # Log the results
    logging.info(f"CPU Usage: {cpu}%, Memory Usage: {memory}%, Disk Usage: {disk}%, Process Count: {processes}")
if _name_ == "_main_":
    system_health_check()
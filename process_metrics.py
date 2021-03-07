import psutil
import argparse
import time
import csv
import warnings

def get_process_info(process_name, duration, sampling):
    # the list the contain all process dictionaries
    processes = []

    memory_leak_threshold = 10

    with open('output.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["PID", "Name", "CPU Percent", "Memory Info", "Open Files"])

        pid = check_if_procerss_running(process_name)
        if pid:
            process = psutil.Process(pid)

            # get all process info in one shot
            t_end = time.time() + int(duration)
            while time.time() < t_end:
                # do whatever you do
                cpu_percent = process.cpu_percent(interval=float(sampling))
                memory_info = process.memory_info()
                memory_percent = process.memory_percent()
                if memory_percent > memory_leak_threshold:
                    warnings.warn('Possible memory leak with ' + process_name)
                open_files = process.open_files()
                writer.writerow([pid, process_name, cpu_percent, memory_info, memory_percent, open_files])
        else:
            print('Pls enter running process name.')


def check_if_procerss_running(process_name):
    '''
    Check if there is any running process that contains the given name process_name.
    '''
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if process_name.lower() in proc.name().lower():
                return proc.pid
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False


def check_positive(value):
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError("%s is an invalid positive int value" % value)
    return ivalue

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--process_name", required=True, help="Enter process name")
parser.add_argument("-d", "--duration", required=True, type=check_positive, help="Enter overall duration of the monitoring in seconds")
parser.add_argument("-s", "--sampling", default=5, help="Enter sampling interval")

args = parser.parse_args()
print(args.process_name)
print(args.duration)
print(args.sampling)

get_process_info(args.process_name, args.duration, args.sampling)



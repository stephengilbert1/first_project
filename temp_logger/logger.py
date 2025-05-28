from datetime import datetime

def log_conversion(celsius, fahrenheit, kelvin, log_file="temperature_log.csv"):
    timestamp = datetime.now().isoformat()
    with open(log_file, "a") as file:
        file.write(f"{timestamp},{celsius},{fahrenheit},{kelvin}\n")

def read_log(log_file="temperature_log.csv"):
    try:
        with open(log_file, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        return None
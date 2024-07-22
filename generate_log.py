import random
import datetime
from datetime import datetime
import time
from tokenize import Ignore

log_file = "application_log.log"

log_levels = ["INFO", "DEBUG", "WARN", "ERROR", "TRACE"]

status = ["SUCSESS", "FAILD", "TIMEOUT"]

response_time = ["0.1", "0.5", "0.9", "1", "5"]

request_methods = ["GET", "PUT", "POST", "PATCH", "UPD"]

api_names = ["user_manegement"]

api_endpoints = {
    "user_manegement" : ["list_user", "auth"]
}

print("weite a log file")
with open(log_file, "w") as f:
    for i in range(100):
        log_levels = random.choice(log_levels)
        log_status = random.choice(status)
        response_time = random.choice(response_time)
        api_names = random.choice(api_names)

        # endpoint = random.choice(api_endpoints[api_names])

        log_entry = f"{datetime.now()}   {log_levels}   {log_status}   {response_time}   {api_names}   THIS IS THE FINAL LOG OF THIS TIME"

        f.write(log_entry+ "\n")
        time.sleep(random.uniform(0.01,0.02))

print("log file getattr")
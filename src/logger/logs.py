import logging
import os
from datetime import datetime

# Let's Desing our Logger file
# 1. Create folder
# 2. if our folders are avaliable in this case we can create file only 
# 3. capture complete information about logs like timing, ip address, message, 
# 4. our basicconfig


# 80 % -> prediction -> 1m -> predcued our params -> 76% 40 sec for single prediction and batch
# model registory -> mutiple pkl -> model.pkl, 



# Creating logs directory to store log in files
LOG_DIR = "logs"
LOG_DIR = os.path.join(os.getcwd(), LOG_DIR)

#Creating LOG_DIR if it does not exists.
os.makedirs(LOG_DIR, exist_ok=True)


# Creating file name for log file based on current timestamp
CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"
file_name = f"log_{CURRENT_TIME_STAMP}.log"

#Creating file path for projects.
log_file_path = os.path.join(LOG_DIR, file_name)


logging.basicConfig(filename=log_file_path,
                    filemode='w',
                    format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)





# 100 









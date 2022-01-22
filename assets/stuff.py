# Imports
from datetime import datetime


# Logs function
def log(type, user_id=0):
    if type == 'init':
        log_file = open("logs/logs.txt", "a", encoding="utf-8")
        log_file.write(f'{str(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))}\nBot started\n\n')
        log_file.close
    elif type == 'new_user':
        log_file = open("logs/logs.txt", "a", encoding="utf-8")
        log_file.write(f'{str(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))}\nNew user added || {str(user_id)}\n\n')
        log_file.close
    elif type == 'nh_id_added':
        log_file = open("logs/logs.txt", "a", encoding="utf-8")
        log_file.write(f'{str(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))}\nNew NiceHash id added || {str(user_id)}\n\n')
        log_file.close

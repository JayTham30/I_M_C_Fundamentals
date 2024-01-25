import csv
import random
import time
import shutil
from datetime import datetime

def read_csv(file_path):
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            header = next(reader)
            data = list(reader)
        return header, data
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None, None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None, None

def write_csv(file_path, header, data):
    try:
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(data)
        print(f"Data written to {file_path} successfully.")
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except Exception as e:
        print(f"Error writing to file: {e}")

def backup_original(file_path, backup_dir):
    file_name = file_path.split("/")[-1]
    backup_path = f"{backup_dir}/{file_name}"
    shutil.copy2(file_path, backup_path)
    return backup_path

def shuffle_write_csv(file_path, header, data):
    random.shuffle(data)
    write_csv(file_path, header, data)

def main(csv_file_path, backup_dir, shuffle_time, backup_interval):
    while True:
        current_time = datetime.now().strftime("%H:%M")

        if current_time == shuffle_time:
            today = datetime.today().strftime("%Y-%m-%d")
            backup_done_flag = f"backup_done_{today}.txt"
            
            if not os.path.exists(os.path.join(backup_dir, backup_done_flag)):
                header, data = read_csv(csv_file_path)

                if header is not None and data is not None:
                    backup_path = backup_original(csv_file_path, backup_dir)
                    
                    if backup_path:
                        print(f"Backup created at: {backup_path}")
                        
                        shuffle_write_csv(csv_file_path, header, data)
                        print("Data shuffled successfully.")
                        
                        with open(os.path.join(backup_dir, backup_done_flag), 'w') as flag_file:
                            flag_file.write("Backup done for today.")

        time.sleep(backup_interval)

if __name__ == "__main__":
    print("hello")

    import os

    # Configuration
    # csv_file_path = "C:\Users\Jay Thammavongsa\IMC_Fundamentals\sales_data.csv"
    # backup_dir = "C:\Users\Jay Thammavongsa\backup_directory"
    csv_file_path = "C:\\Users\\Jay Thammavongsa\\IMC_Fundamentals\\sales_data.csv"
    backup_dir = "C:\\Users\\Jay Thammavongsa\\backup_directory"

    shuffle_time = "14:00"  # Time for shuffle set in a 24-hr format
    backup_interval = 10  # Interval in seconds

    # Execute the main function
    main(csv_file_path, backup_dir, shuffle_time, backup_interval)

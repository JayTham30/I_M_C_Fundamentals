import csv
import random
import time
import shutil
from datetime import datetime

def read_csv(file_path):
    try:
        #Opens up file path and reads. skips over the header on csv file. list the data on the csv file.
        with open(file_path, "r") as file:
            file_reader = csv.reader(file)
            header = next(file_reader)
            data = list(file_reader)
        return header, data
    except FileNotFoundError:
        #Gives print message if FileNotFoundError comes up
        print(f"the file {file_path} was not found")
        return None, None
    except Exception as e:
        #Catches all general types of error and prints message given.
        print(f"Error reading file{e}")
        return None, None


def write_csv(file_path, header, data):
    #Opens up file path, writes, and creates newline on str. Writes into file. Writerow used to write the header. Writerows used to write the data. 
    with open(file_path, "w", newline='') as file:
        file_writer = csv.writer(file)
        file_writer.writerow(header)
        file_writer.writerows(data)

def backup_original(file_path, backup_dir):
    #Getting the file name by splitting and indexing into the end of the file path.
    file_name = file_path.split("/")[-1]
    #Creates the full path of the backup_path by using an fstring and combining the backup_dir and file_name
    backup_path = f"{backup_dir}/{file_name}"
    #Copying original file(file_path) to the backup file(backup_path)
    shutil.copy2(file_path, backup_path)
    return backup_path
   
def shuffle_write_csv(file_path, header, data):
    #Uses the random fuction to shuffle the rows in the "data" list.
    random.shuffle(data)
    #calls the fuction to write the shuffled data back to the original csc file.
    write_csv(file_path, header, data)

def main():
    #The path to the CSV file containing the sales data.
    sale_file_path = "C:\\Users\\Jay Thammavongsa\\IMC_Fundamentals\\sales_data.csv"
    #The directory where backup files will be stored.
    backup_directory = "C:\\Users\\Jay Thammavongsa\\backup_directory"
    #The time of day (in 24-hour format) when the shuffle operation should occur.
    shuffle_time = "14:00"


    #Retrieves the current date in the format "YYYY-MM-DD"
    today = datetime.today().strftime("%Y-%m-%d")
    #A flag indicating whether a backup has been done for the current day.
    backup_done = False

    #Infinite loop
    while True:
        #Retrieves the current time in "HH:MM" format.
        current_time = datetime.now().strftime("%H:%M")

        if current_time == shuffle_time and not backup_done:
            header, data = read_csv(sale_file_path)

            if header is not None and data is not None:
                backup_path = backup_original(sale_file_path, backup_directory)
                if backup_path:
                    print(f"Backup created at: {backup_path}")
                    shuffle_write_csv(sale_file_path, header, data)
                    print("Data shuffled successfully.")
                    backup_done = True
            else:
                print("Skipping shuffle due to file read error.")
        
        elif current_time != shuffle_time:
            backup_done = False

        time.sleep(10)



if __name__ == "__main__":
    main()





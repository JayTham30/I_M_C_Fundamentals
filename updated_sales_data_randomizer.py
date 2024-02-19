import csv
import random
import shutil
import time
import os
import datetime

# Function to shuffle rows in the CSV file
def shuffle_csv(filename):
    # Open the CSV file for reading
    with open(filename, 'r', newline='') as csvfile:
        # Create a CSV reader object
        reader = csv.reader(csvfile)
        # Read the header row
        header = next(reader)
        # Read the remaining data rows into a list
        data = list(reader)
        # Shuffle the data rows
        random.shuffle(data)
    
    # Open the CSV file for writing
    with open(filename, 'w', newline='') as csvfile:
        # Create a CSV writer object
        writer = csv.writer(csvfile)
        # Write the header row back to the file
        writer.writerow(header)
        # Write the shuffled data rows back to the file
        writer.writerows(data)

# Function to backup the original file
def backup_file(filename, backup_dir):
    # Check if the backup directory exists, if not, create it
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    # Construct the backup filename based on the current date
    backup_filename = os.path.join(backup_dir, f"backup_{datetime.date.today()}.csv")
    # Copy the original file to the backup directory
    shutil.copy(filename, backup_filename)

# Main function
def main():
    # Define the filename of the sales data file
    sales_data_file = 'sales_data.csv'
    # Define the directory for storing backup files
    backup_directory = 'backup'
    # Construct the backup filename based on the current date
    backup_filename = f"backup_{datetime.date.today()}.csv"
    
    # Backup the original file if it hasn't been backed up today
    if not os.path.exists(os.path.join(backup_directory, backup_filename)):
        backup_file(sales_data_file, backup_directory)
        print(f"Backup created: {backup_filename}")
    
    # Shuffle the rows of the CSV file
    shuffle_csv(sales_data_file)
    print("Sales data shuffled.")
    
# Run the main function every 10 seconds
if __name__ == "__main__":
    while True:
        main()
        # Wait for 10 seconds before repeating the operation
        time.sleep(10)

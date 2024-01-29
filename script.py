import os
import shutil
import datetime
import schedule
import time

def get_backup_frequency():
    while True:
        frequency = input("Choose backup frequency \nd -> daily\nw -> weekly\ny -> yearly\nEnter: ").lower()
        if frequency in ["d", "w", "y"]:
            return frequency
        else:
            print("Invalid input. Please enter 'd', 'w', or 'y'.")

source_dir = input('Enter the source directory: ')
destination_dir = input('Enter the destination directory: ')
backup_frequency = get_backup_frequency()

if backup_frequency =='w':
    day_of_week = input("Enter the day for the weekly backup (e.g., Monday): ")

bTime = input('Enter the backup time (in HH:MM format): ')

def copy_folder_to_directory(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))

    try:
        shutil.copytree(source, dest_dir)
        print(f"Folder copied to: {dest_dir}")
    except FileExistsError:
        print(f"Folder already exists in: {dest}")

if backup_frequency == 'daily':
    schedule.every().day.at(bTime).do(lambda: copy_folder_to_directory(source_dir, destination_dir))
elif backup_frequency == 'weekly':
    schedule.every().week.day.at(bTime).do(lambda: copy_folder_to_directory(source_dir, destination_dir)).day.at(day_of_week)
elif backup_frequency == 'yearly':
    # Assuming the backup time and day are the same every year
    day_of_year = input("Enter the day of the year for the yearly backup (1 to 365): ")
    schedule.every().year.at(bTime).do(lambda: copy_folder_to_directory(source_dir, destination_dir)).day.at(day_of_year)

while True:
    schedule.run_pending()
    time.sleep(60)

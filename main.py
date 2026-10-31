# Automated File & Directory Organizer
# Built independently to manage desktop clutter automatically by file extension.

import os
import shutil

def organize_folder(target_directory):
    if not os.path.exists(target_directory):
        print("Directory does not exist.")
        return

    for filename in os.listdir(target_directory):
        file_path = os.path.join(target_directory, filename)
        if os.path.isfile(file_path):
            file_extension = filename.split('.')[-1]
            folder_path = os.path.join(target_directory, file_extension.upper() + "_Files")
            
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            
            shutil.move(file_path, os.path.join(folder_path, filename))
            print(f"Moved: {filename} -> {folder_path}")

if __name__ == "__main__":
    print("Task Organizer Initialized...")

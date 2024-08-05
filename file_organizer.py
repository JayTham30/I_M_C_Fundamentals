import os
import shutil

 




# Getting users path to the directory they want to organize. Also checks and ensure that the path is valid 
def get_user_path():
    print("to get started we will need to know the path to the directory you would like to orgranize. ")
    user_path = input("Please enter the path here: ")

    # Checks if path exists
    if os.path.exists(user_path):
        print("good")
        return user_path
    else:
        print("The path you provided does not exist. Please try again. ")
        return get_user_path()


def ogranize_file(path):
    # Dic where Keys are file ext. and Values are correesponding folder names.
    mapping = {
        '.jpg': 'Images',
        '.jpeg': 'Images',
        '.png': 'Images',
        '.gif': 'Images',
        '.pdf': 'PDF',
        '.docx': 'Documents',
        '.txt': 'Documents',
        '.mp3': 'Audio',
        '.wav': 'Audio',
        '.mp4': 'Videos',
        '.mov': 'Videos',
        '.avi': 'Videos'
        }
    
    # Create dic for each file type
    for folder in set(mapping.values()):
        folder_path = os.path.join(path, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isfile(item_path):
            file_extension = os.path.splitext(item)[1]
            if file_extension in mapping:
                folder_name = mapping[file_extension]
                shutil.move(item_path, os.path.join(path, folder_name, item))

    


# Main loop
def main():
    # Introduction
    answer = input('This Program will tidie up your files in a specified directory by orgranizing them into folders based on their file/extension.\nI will just to ask you a few questions.\n-If you would like to continue please enter "Y".\n-If you would like to end the program please enter "N"\n')

    if answer.capitalize() == "Y":
        get_user_path()
    elif answer.capitalize() == "N":
        print("Program Ended.")
    else:
        print('Invalid input. Please enter "Y" or "N".')


main()



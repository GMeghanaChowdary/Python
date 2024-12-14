import os
import shutil
def file_organizer():
    directory = input("Enter the directory path: ")
    files = os.listdir(directory)
    for file in files:
        if file.endswith('.txt'):
            shutil.move(os.path.join(directory, file), os.path.join(directory, 'Text_Files', file))
        elif file.endswith('.jpg'):
            shutil.move(os.path.join(directory, file), os.path.join(directory, 'Images', file))
file_organizer()

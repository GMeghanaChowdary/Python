import os
import string
def search_engine():
    directory = input("Enter the directory to search: ")
    query = input("Enter search query: ").lower()
    files = os.listdir(directory)
    for file in files:
        if query in file.lower():
            print(f"Found: {file}")
search_engine()

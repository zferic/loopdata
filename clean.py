import os

# Define the root directory where you want to start
root_dir = '/media/zman/extrahd/data/loops'

# Define the files you want to remove
files_to_remove = ['desc.txt', 'MakeFile', 'output.txt', 'stuff.py', 'stuff2.py']

# Function to remove files in a directory
def remove_files_in_directory(directory):
    for file_name in files_to_remove:
        file_path = os.path.join(directory, file_name)
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"Removed: {file_path}")
        else:
            print(f"Not found: {file_path}")

# Function to recursively traverse directories
def traverse_directories(root):
    for dir_path, _, _ in os.walk(root):
        remove_files_in_directory(dir_path)

# Start traversing directories
traverse_directories(root_dir)

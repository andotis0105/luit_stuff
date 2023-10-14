import os

# Get current working directory
cw_directory = os.getcwd()

# List all the files in directory
files = os.listdir(cw_directory)

# Create new empty list for file dictionaries
file_info_list = []

# Iterate through each file in the list
for each in files:
    file_path = os.path.join(cw_directory, each)

    # Checks if it's a file  
    if os.path.isfile(file_path):
        # If file, gets the file information
        file_info = {
            "File Name": each,
            "File Size (bytes)": os.path.getsize(file_path),
            "File Type": each.split('.')[-1],  # Gets file extension
        }
        file_info_list.append(file_info)

# Print list of dictionaries
for file_info in file_info_list:
    print(file_info)

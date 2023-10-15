import os

def get_info(directory):
    file_info_list = []

    for root, dirs, files in os.walk(directory): # This part makes it recursive
        for file in files:
            file_path = os.path.join(root, file) 

            file_info = {
                "File Name": file,
                "File Size (bytes)": os.path.getsize(file_path),
                "File Type": file.split('.')[-1],  # Gets file extension
                "File Path": file_path,
            }
            file_info_list.append(file_info)

    return file_info_list

# Gets current working directory
cw_directory = os.getcwd()

file_info_list = get_info(cw_directory)

# Print list of dictionaies 
for file_info in file_info_list:
    print(file_info)

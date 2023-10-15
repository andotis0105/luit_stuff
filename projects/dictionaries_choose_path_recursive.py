import os

# Instructions because I don't like text input boxes after a long line of text
print('--Input desired directory below, or hit Enter for the current directory.-- ')

# This function clearly gets the file information
def get_file_info(directory):
    file_info_list = []
    for root, dirs, files in os.walk(directory): # Makes it recursive
        for each in files:
            file_path = os.path.join(root, each)

            file_info = {
                "File Name": each,
                "File Size (bytes)": os.path.getsize(file_path),
                "File Type": each.split('.')[-1],  # Gets the file extension
                "File Path": file_path, # States full directory path for the file
            }
            file_info_list.append(file_info) # Puts it all together in a list
    return file_info_list

def choose_directory(): 
    path = input("Directory: ") # Allows user input of directory path.
    if not path: 
        path = os.getcwd() # Defaults to current working directory if no path is given
    else:
        path = os.path.abspath(path)  # Converts the input path to an absolute path (so chosen directory is also recursive)

    result = get_file_info(path)
    for item in result:
        print(item)

if __name__ == "__main__":
    choose_directory()

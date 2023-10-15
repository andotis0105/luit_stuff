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

def choose_directory(): # Allows user input or defaults to the current working directory
    path = input("Directory: ") # Need to put the whole file path (ex ../OtisCorp_ship_parts_Engines)
    if not path: # If no directory is specified, 
        path = os.getcwd() 

    result = get_file_info(path)
    print(result)

if __name__ == "__main__":
    choose_directory()

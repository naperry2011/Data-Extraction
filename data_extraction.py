import os
# let's start off by importing operating systems

# Get the list of files in the working directory
files = os.listdir()

# Create a list to store the file information
file_info_list = []

# Loop through the files and gather information
for file in files:
    if os.path.isfile(file):
        file_info = {
            "name": file,
            "size": os.path.getsize(file)
        }
        file_info_list.append(file_info)

# Print the list of dictionaries
print(file_info_list)

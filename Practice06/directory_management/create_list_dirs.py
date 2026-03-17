# create nested directories by using the "os" module

import os
#create nested directories
os.makedirs("Practice06/test_folder/inner_folder", exist_ok=True)

print("Directories created")

# list all folders and files in the current working folder

print("\nAll items in Practice06: ")
items = os.listdir("Practice06")
for item in items:
    if item.endswith(".txt"):
       print(item)

os.rmdir("Practice06/test_folder/inner_folder")
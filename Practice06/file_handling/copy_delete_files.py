# copying and creating a backup txt file

import shutil 
shutil.copy("../sample.txt", "../backup_copy_sample.txt")

with open("../backup_copy_sample.txt", "r") as f:
    print(f.read())


# to delete the txt file: we use the os library in python 
# we import os, then we use: os.remove()

"""
import os

file_path = "../backup_copy_sample.txt"

if os.path.exists(file_path):
   os.remove(file_path)
   print("the file has been delated successfully")
else:
    print("file not found")
"""
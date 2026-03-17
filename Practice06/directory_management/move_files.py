# moving files from one destination to another 

import shutil
import os

source = "Practice06/sample.txt"
destination = "Practice06/test_folder/backup_copy_sample.txt"

if os.path.exists(source):
    shutil.copy(source, destination)
    print("file copied successfully")
else:
    print("source file was not found")
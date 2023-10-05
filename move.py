import os
import shutil

from_dir = "C:/Users/Downloads"
to_dir = "C:/Users/Desktop/Downloaded_Files"



list_of_files = os.listdir(from_dir)
print(list_of_files)
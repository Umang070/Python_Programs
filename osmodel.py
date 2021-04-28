# ------------import os--------

import os

# print(os.getcwd())

# if os.path.exists("notpad file"):
#         print("already exist")
# else:
#         os.mkdir("notpad file")

# os.chdir(r"U:\python_prog")
# print(os.listdir())
# print(os.listdir(r"C:\youtube"))

# open("temp.txt","a").close()

# os.mkdir(r"C:\youtube\temp_fol")

# --------for full path of folder and files (DEFTH FIRST SEARCH)-------

# for item in os.listdir():   #not depth...
#     path = os.path.join(os.getcwd(),item)
#     print(path)

# file_depth = os.walk(r"U:\python_prog")
# for cur_path,folder_name,file_name in file_depth:
#     print(f"Current Path is : {cur_path}")
#     print(f"Folder Name is : {folder_name}")
#     print(f"File Name is : {file_name}")
    
# os.rmdir("notpad file")

#------------import shutil---------

import shutil

# shutil.rmtree("notpad file")
# shutil.copy(r"osmodel.py","C:\youtube/new.py")...#for file and for foldeer copytree.

shutil.move(r"osmodel.py","U:\python_prog/osmodel.py")
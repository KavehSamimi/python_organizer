
import os 
import shutil

directory_path = input('Please enter the path of the folder that you need organized: ')
files = os.listdir(directory_path)


for file in files:
    filename, extension = os.path.splitext(file)
    extension= extension[1:] # just need the extension name, so I removed the '.' using slicing. 
    
    # if the directory that the file belongs to already exists, move the file into it. 
    if os.path.exists(os.path.join(directory_path, extension)):
        shutil.move(os.path.join(directory_path, file), os.path.join(directory_path, extension, file))
        
        
    else: # if the directory does not exists, create a directory and move the file into it. 
        os.makedirs(os.path.join(directory_path, extension))
        shutil.move(os.path.join(directory_path, file), os.path.join(directory_path, extension, file))
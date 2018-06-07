import shutil
import os

addToRootPath = os.path.join(os.getcwd(), 'add-to-root')
# shutil.copytree(os.path.join(filePath, 'add-to-root', "dll-files"), os.path.join(filePath, 'dist') )

for folderName in os.listdir(addToRootPath):
    for fileName in os.listdir(os.path.join(addToRootPath, folderName)):
        shutil.copy(os.path.join(addToRootPath, folderName, fileName), os.path.join(os.getcwd(), 'dist', fileName))

# print("Hello World!")
# input() # holds command prompt open until input
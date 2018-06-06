import os
import sys
import shutil

rootDir = 'C:\\' # Windows
# rootDir = '~'  # Linux

# define the file that will be converted to .exe
fileName = 'hello.py' 
# define the file path of the file that will be converted.
# default value is current working directory or cwd (pwd)
filePath = os.getcwd()
# where cxfreeze is installed on your local machine
# This might be in C:\\python36\Scripts\cxfreeze
# cxfreeze is not a path but the cxfreeze library
cxFreezePath = os.path.join(rootDir, "python36", "Scripts", "cxfreeze")

if os.path.isdir(filePath):
    if os.path.isfile(os.path.join(filePath, fileName)):
        # define python3 cxfreeze file path
        path = cxFreezePath
        # Run python process of converting .py to .exe
        os.system("python " + path + " " + os.path.join(filePath, fileName))
        # fix missing VCRUNTIME140.dll
        shutil.copyfile(os.path.join(filePath, 'dll-files', 'vcruntime140.dll'), os.path.join(filePath, 'dist', 'vcruntime140.dll'))
    else:
        print("File: {} not found.".format(fileName))
else:
    print("Directory: {} not found.".format(filePath))








# py3exe - Convert Python3 .py to .exe (ver 1.2)

### Required Pip Install. Choose either
```bash
pip install cx_Freeze
python -m pip install cx_Freeze
```

## Why might this be needed?

Python3 won't always be available on every environment. Sometimes the network security team will only allow .exe files or they may not want to install another bit of software on a server.

This make the .py application self-contiained and portable.

## Required Setup

Windows environments require the use of two back slashes. The first slash says to ignore the second. Windows...!

1. Install cx_Freeze
2. Set system root directory
    ```python
    rootDir = 'C:\\' # Windows
    ```
3. Define the .py file that will get converted to .exe
    ```python
    fileName = 'hello.py'
    ```
4. Define the file path where the file located. 

    > If you placed py3exe.py in the same directory as the file you are converting, such as...
    ```bash
    py3exe.py
    hello.py
    ```
    > Then you can use the default which is the current working directory **(recommended)**
    ```python
    filePath = os.getcwd()
    ```
    > Otherwise you need to specify the absolute path.
    ```python
    filePath = 'C:\\Users\\DrJonesy\\Documents\\current-working-folder'
    ```
    > An alternative for setting the absolute path is
    ```python
    filePath = os.path.join(rootDir, 'Users', 'DrJonesy', 'Document','current-working-folder')
    ```
5. Define the python3 location to cxfreeze on your local machine
    ```bash
    cxFreezePath = os.path.join(rootDir, "python36", "Scripts", "cxfreeze")
    ```
    > **rootDir** points to the variable "rootdir", **python36** is the folder where this version of python3 is installed, **Scripts** should be in the python36 folder, and **cxfreeze** is the Script.

6. In your command window or terminal run the command:
    ```bash
    python py3exe.py
    ```

7. This will run through a process and create a folder called **dist**

# "dist" Folder Structure
```bash
lib\ (folder)
hello.exe (or your file name)
python36.dll
vcruntime140.dll
```
The **lib** folder contains all the packages and python file needed to run your application on any environment.

### Thank You
The program was adapted from the YouTube video:
https://www.youtube.com/watch?v=gOV3AWiQclg by Technological

### Errors
* Missing VCRUNTIME140.dll [SOLVED] 
(if you encounter issues concerning missing .dll files the refer to the syntax for line 25)


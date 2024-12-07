# Zipping a Folder

## Overview
This Python program zips a folder and its contents (including subdirectories) into a `.zip` file while preserving the folder structure. The output `.zip` file is created in the same directory as the original folder.



## How to Run the Program

### Prerequisites
- Python 3.x must be installed on your system.
- Ensure the folder to be zipped exists and you have the necessary permissions to access it.

### Steps to Execute
1. Save the script in a file (e.g., `zip_folder.py`).
2. Open a terminal or command prompt.
3. Run the script:
   ```bash
   python zip_folder.py
   ```
4. Provide the full path to the folder when prompted:
   ```
   Please enter the path to the folder you want to zip: /path/to/folder
   ```



## Example Execution

### Input Folder Structure:
```
/my_folder/
├── file1.txt
├── file2.txt
└── subfolder/
    ├── file3.txt
    └── file4.txt
```

### Program Output:
A `.zip` file named `my_folder.zip` is created in the same directory:
```
/my_folder.zip
```

### Output Folder Structure Inside ZIP:
```
/my_folder/
├── file1.txt
├── file2.txt
└── subfolder/
    ├── file3.txt
    └── file4.txt
```



## Features
1. Automatically creates a `.zip` file with the same name as the folder.
2. Preserves the original folder structure inside the `.zip` file.
3. Handles invalid folder paths, permission issues, and empty folders gracefully.
4. Provides detailed messages about the zipping process.

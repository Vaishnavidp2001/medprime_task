# Renaming Files Sequentially in a Folder

## Objective
This program renames all files in a specified folder by numbering them sequentially, starting from 1, while retaining the original file extensions.

## Features
1. Validates the folder path to ensure it exists and contains files.
2. Renames files sequentially in the format `1.ext`, `2.ext`, ..., where `.ext` is the original file extension.
3. Handles errors, such as invalid paths, empty folders, or permission issues.
4. Ignores subdirectories and hidden files.

## Usage
1. Run the program in a Python environment.
2. Enter the full path to the folder containing files when prompted.
3. The program will rename the files sequentially and display the changes.

## Input Example
C:\Users\Shree\OneDrive\Desktop\Task\medprime\Assisment1\my_folder




## Edge Cases
1. **Empty Folder**: Displays a message, "The folder is empty. No files to rename."
2. **Invalid Path**: Displays an error message if the folder path does not exist or is not a directory.
3. **Permission Issues**: Skips files that cannot be renamed and displays an error message.

## Requirements
- Python 3.x

## Example Folder Structure (Before)
```
my_folder/ 
├── image1.jpg 
├── document.txt 
├── report.pdf
├── notes.docx 
├── music.mp3
```

## Example Folder Structure (After)
```my_folder/ 
├── 1.jpg 
├── 2.txt 
├── 3.pdf 
├── 4.docx 
├── 5.mp3
```



## Assumptions
- The folder contains only files to rename (subdirectories are ignored).
- The files are named in ascending order based on their original names.

## Running the Script
1. Save the script in a file, e.g., `rename_files.py`.
2. Run the script from the terminal or IDE.
3. Provide the folder path when prompted.





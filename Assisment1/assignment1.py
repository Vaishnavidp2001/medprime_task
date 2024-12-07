import os

def validate_folder(folder_path):
    if not os.path.exists(folder_path):
        return f"Error: The folder '{folder_path}' does not exist."
    if not os.path.isdir(folder_path):
        return f"Error: The path '{folder_path}' is not a folder."
    
    files = [file for file in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, file))]
    if not files:
        return "The folder is empty. No files to rename."
    
    return files

def rename_files_sequentially(folder_path):

    files = validate_folder(folder_path)
    if isinstance(files, str): 
        print(files)
        return

    print("Renaming files...")
    for index, file_name in enumerate(sorted(files), start=1):
       
        _, file_extension = os.path.splitext(file_name)
        

        new_name = f"{index}{file_extension}"
        

        old_path = os.path.join(folder_path, file_name)
        new_path = os.path.join(folder_path, new_name)
        try:
            os.rename(old_path, new_path)
            print(f"File '{file_name}' renamed to '{new_name}'")
        except Exception as e:
            print(f"Error renaming file '{file_name}': {e}")

    print("Renaming completed.")


if __name__ == "__main__":
    
    folder_path = input("Please enter the path to the folder: ").strip()
    rename_files_sequentially(folder_path)

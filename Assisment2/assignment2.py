import os
import zipfile

def zip_folder(folder_path):
    if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
        print(f"Error: The folder '{folder_path}' does not exist or is not a directory.")
        return
    

    folder_name = os.path.basename(folder_path.rstrip(os.sep))
    zip_file_name = f"{folder_name}.zip"
    zip_file_path = os.path.join(os.path.dirname(folder_path), zip_file_name)
    
    print(f"Zipping the folder '{folder_path}' into '{zip_file_path}'...")
    
    try:
        with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    relative_path = os.path.relpath(file_path, folder_path)
                    zipf.write(file_path, relative_path)
        
        print(f"Successfully created ZIP file: {zip_file_path}")
    except PermissionError:
        print(f"Error: Permission denied while creating '{zip_file_path}'.")
    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}")


def main():
    folder_path = input("Please enter the path to the folder you want to zip: ").strip()
    zip_folder(folder_path)

if __name__ == "__main__":
    main()

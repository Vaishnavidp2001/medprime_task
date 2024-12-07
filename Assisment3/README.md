
# Collage Creator Program

## Overview
The Collage Creator Program is a Python script that combines four input images into a 2x2 collage. The resulting collage is saved as a single image file in the specified output format, maintaining the original quality of the images.


## Features
- Accepts four input image paths from the user.
- Resizes images to ensure uniform dimensions for the collage.
- Creates a 2x2 grid of the input images.
- Allows users to specify the desired output format (e.g., JPG, PNG).
- Handles errors like invalid image paths or unsupported file formats.


## Prerequisites
- Python 3.7+
- Pillow Library (Python Imaging Library)

To install Pillow, run:
```bash
pip install pillow
```


## How to Run the Program

1. Download the Script:
   Save the `create_collage.py` file to your computer.

2. Open a Terminal or Command Prompt:
   Navigate to the directory where the script is saved.

3. Run the Script:
   Use the following command:
   ```bash
   python create_collage.py
   ```

4. Provide Input:
   - Enter the file paths of the four images when prompted.
   - Specify the desired output file format (e.g., `jpg` or `png`).

5. View Output:
   The collage will be created and saved as `collage.<format>` in the current directory.


## Example Usage

Input:
```plaintext
Please enter the path for Image 1: C:\path\to\image1.jpg
Please enter the path for Image 2: C:\path\to\image2.jpg
Please enter the path for Image 3: C:\path\to\image3.jpg
Please enter the path for Image 4: C:\path\to\image4.jpg
Please specify the output file format (e.g., jpg, png): jpg
```

Output:
- A new file named `collage.jpg` containing a 2x2 grid of the input images.


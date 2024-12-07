from PIL import Image
import os

def get_image_paths():
    paths = []
    for i in range(1, 5):
        path = input(f"Please enter the path for Image {i}: ").strip()
        if not os.path.isfile(path):
            print(f"Error: The file at '{path}' does not exist or is not a valid file.")
            return None
        try:
            Image.open(path).verify()
        except Exception:
            print(f"Error: The file at '{path}' is not a valid image.")
            return None
        paths.append(path)
    return paths

def resize_images(images, target_size):
    resized_images = []
    for img in images:
        resized_images.append(img.resize(target_size, Image.Resampling.LANCZOS))
    return resized_images

def create_collage(image_paths, output_file="collage.jpg"):
    try:
        images = [Image.open(path) for path in image_paths]

        min_width = min(img.width for img in images)
        min_height = min(img.height for img in images)


        resized_images = resize_images(images, (min_width, min_height))


        collage_width = min_width * 2
        collage_height = min_height * 2
        collage = Image.new("RGB", (collage_width, collage_height))


        collage.paste(resized_images[0], (0, 0))
        collage.paste(resized_images[1], (min_width, 0))
        collage.paste(resized_images[2], (0, min_height))
        collage.paste(resized_images[3], (min_width, min_height))


        collage.save(output_file)
        print(f"Collage created successfully and saved as '{output_file}'!")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("Welcome to the Collage Creator Program!")
    image_paths = get_image_paths()
    if image_paths:
        output_format = input("Please specify the output file format (e.g., jpg, png): ").strip().lower()
        if output_format not in ["jpg", "jpeg", "png"]:
            print("Invalid format! Defaulting to 'jpg'.")
            output_format = "jpg"
        output_file = f"collage.{output_format}"
        create_collage(image_paths, output_file)

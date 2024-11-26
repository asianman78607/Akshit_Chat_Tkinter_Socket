from PIL import Image
import os

def resize_images_in_directory(input_directory, output_directory, new_width, new_height):
    """
    Resizes all images in the input directory and saves them in the output directory.

    :param input_directory: Path to the input directory containing images
    :param output_directory: Path to the output directory to save resized images
    :param new_width: New width for the resized images
    :param new_height: New height for the resized images
    """
    if not os.path.exists(input_directory):
        print(f"The directory {input_directory} does not exist.")
        return

    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    # Process each file in the directory
    for filename in os.listdir(input_directory):
        input_path = os.path.join(input_directory, filename)

        # Skip directories
        if not os.path.isfile(input_path):
            continue

        try:
            # Open the image
            with Image.open(input_path) as img:
                # Resize the image
                resized_img = img.resize((new_width, new_height))

                # Save the resized image to the output directory
                output_path = os.path.join(output_directory, filename)
                resized_img.save(output_path)
                print(f"Resized and saved: {output_path}")

        except Exception as e:
            print(f"Error processing {filename}\\")

if __name__ == "__main__":
    # Input paths and resize dimensions
    input_dir = input("Enter the path to the input directory: ").strip()
    output_dir = input("Enter the path to the output directory: ").strip()
    width = int(input("Enter the new width for the images: ").strip())
    height = int(input("Enter the new height for the images: ").strip())

    # Resize images
    resize_images_in_directory(input_dir, output_dir, width, height)

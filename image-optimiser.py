import os
from PIL import Image
import random

def resize_images(source_folder=None, dest_folder_name="optimised", width=None):
    """Resizes and compresses all images in source_folder and saves them in JPEG format in a sub-folder."""
    
    # If no source_folder is provided, use the current directory of the script
    if source_folder is None:
        source_folder = os.path.dirname(os.path.abspath(__file__))
    
    dest_folder = os.path.join(source_folder, dest_folder_name)
    
    # Create destination folder if it doesn't exist
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)
        
        # Check if the file is an image
        if os.path.isfile(file_path) and file_path.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff', '.heic')):
            try:
                with Image.open(file_path) as im:
                    # If width is provided, calculate height to maintain aspect ratio
                    if width:
                        w_percent = width / float(im.size[0])
                        height = int((float(im.size[1]) * float(w_percent)))
                        new_size = (width, height)
                    else:
                        new_size = im.size
                    
                    # Resize
                    img_resized = im.resize(new_size)
                    
                    # Change the filename to have a .jpg extension
                    new_filename = os.path.splitext(filename)[0] + '.jpg'
                    dest_path = os.path.join(dest_folder, new_filename)

                    # Save resized and compressed image in JPEG format
                    img_resized.save(dest_path, "JPEG", quality=65)
            except Exception as e:
                print("Unable to process {}. Reason: {}".format(filename, e))

# Usage
width = random.randint(1300, 1800)
resize_images(width=width)

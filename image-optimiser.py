import os
from PIL import Image

def resize_images(source_folder=None, dest_folder_name="optimised", width=None):
    """Resizes and compresses all images in source_folder and saves them in a sub-folder."""
    
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
                im_resized = im.resize(new_size)
                
                # Save resized and compressed image
                dest_path = os.path.join(dest_folder, filename)
                im_resized.save(dest_path, "JPEG", quality=85)
        except Exception as e:
            print(f"Unable to process {filename}. Reason: {e}")

# Usage
resize_images(width=800)

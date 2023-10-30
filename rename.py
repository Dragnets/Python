import os

used_names = set()

def rename_file(file_path, new_name):
    global used_names
    
    _, ext = os.path.splitext(file_path)  # Use the file extension of the original file
    base, _ = os.path.splitext(new_name)  # Ignore the extension from the new name if any
    
    new_name = f"{base.lower()}{ext.lower()}"  # Combine base of new name with original file extension, both in lowercase
    new_path = os.path.join(os.path.dirname(file_path), new_name)
    
    count = 1
    while base.lower() in used_names:  # Check base name without extension
        new_name = f"{base.lower()}_{count}{ext.lower()}"
        new_path = os.path.join(os.path.dirname(file_path), new_name)
        base, _ = os.path.splitext(new_name)  # Update base for the new name
        count += 1
    
    os.rename(file_path, new_path)
    used_names.add(base.lower())  # Add base name without extension to used_names
    print(f"File renamed to: {new_name}")

def rename_files_in_folder(folder_path, names):
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    for file, name in zip(files, names):
        file_path = os.path.join(folder_path, file)
        rename_file(file_path, name)

# Path to the folder containing the images
folder_path = r"C:\Users\Raitis\Desktop\Python\optimised"

# List of new names for the files
names = [
    "scaffold-tower", "frame-scaffold", "tube-scaffold", "modular-scaffold", "system-scaffold", 
    "rolling-scaffold", "suspended-scaffold", "birdcage-scaffold", "single-scaffold", "double-scaffold", 
    "cantilever-scaffold", "hanging-scaffold", "mobile-scaffold", "independent-scaffold", "putlog-scaffold", 
    "trestle-scaffold", "aluminum-scaffold", "steel-scaffold", "access-tower", "scaffold-board", "scaffold-tube", 
    "stair-tower", "facade-scaffold", "perimeter-scaffold", "internal-scaffold", "external-scaffold", 
    "bridge-scaffold", "tunnel-scaffold", "tower-scaffold", "cuplock-scaffold", "kwikstage-scaffold", 
    "layher-scaffold", "haki-scaffold", "multidirectional-scaffold", "fixed-scaffold", "adjustable-scaffold", 
    "protective-scaffold"
]

rename_files_in_folder(folder_path, names)

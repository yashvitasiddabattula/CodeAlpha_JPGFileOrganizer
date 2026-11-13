
import os
import shutil

# Get the current project folder
base_folder = os.path.dirname(os.path.abspath(__file__))

# Define source and destination folders
source_folder = os.path.join(base_folder, "Source_Images")
destination_folder = os.path.join(base_folder, "Organized_Images")

# Create folders if they do not exist
os.makedirs(source_folder, exist_ok=True)
os.makedirs(destination_folder, exist_ok=True)

print("======================================")
print("         JPG FILE ORGANIZER")
print("======================================")

# Count moved files
moved_count = 0

# Read files from the source folder
for filename in os.listdir(source_folder):

    source_path = os.path.join(source_folder, filename)

    # Check whether it is a file with .jpg extension
    if os.path.isfile(source_path) and filename.lower().endswith(".jpg"):

        # Set the destination file path
        destination_path = os.path.join(destination_folder, filename)

        # Avoid overwriting an existing file
        if os.path.exists(destination_path):
            name, extension = os.path.splitext(filename)
            counter = 1

            while os.path.exists(destination_path):
                new_filename = f"{name}_{counter}{extension}"
                destination_path = os.path.join(
                    destination_folder, new_filename
                )
                counter += 1

        # Move the JPG image
        shutil.move(source_path, destination_path)

        print(f"Moved: {filename}")
        moved_count += 1

# Display final result
print("--------------------------------------")
print(f"Total JPG images moved: {moved_count}")

if moved_count == 0:
    print("No JPG images found in the source folder.")

print("File organization completed!")
print("======================================")

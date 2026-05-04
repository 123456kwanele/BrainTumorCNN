import kagglehub
import os
import shutil

# Define where we want the dataset
target_path = "data/raw"

# Create the folder if it doesn't exist
os.makedirs(target_path, exist_ok=True)

print("Downloading dataset...")
print("This may take a few minutes...")

# Download latest version to kagglehub's default cache location
path = kagglehub.dataset_download("masoudnickparvar/brain-tumor-mri-dataset")

print(f"Downloaded to cache: {path}")

# Move files from cache to our data/raw folder
print(f"Moving files to: {target_path}")

# List all files in downloaded path
for item in os.listdir(path):
    source = os.path.join(path, item)
    destination = os.path.join(target_path, item)
    
    # If it's a folder, copy entire folder
    if os.path.isdir(source):
        if os.path.exists(destination):
            print(f"  Removing existing: {destination}")
            shutil.rmtree(destination)
        shutil.copytree(source, destination)
        print(f"  ✅ Copied folder: {item}")
    # If it's a file, copy the file
    else:
        shutil.copy2(source, destination)
        print(f"  ✅ Copied file: {item}")

print("\n✅ Dataset successfully downloaded and placed in data/raw/!")
print(f"Location: {os.path.abspath(target_path)}")
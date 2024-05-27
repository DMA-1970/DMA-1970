import os
import shutil
import filecmp
from pathlib import Path

def should_copy(src_file, dst_file):
    # Check if the destination file exists
    if not os.path.exists(dst_file):
        return True
    # Compare the source and destination files
    return not filecmp.cmp(src_file, dst_file, shallow=False)

def sync_directories(src_dir, dst_dir):
    src_dir = Path(src_dir)
    dst_dir = Path(dst_dir)

    for src_root, _, files in os.walk(src_dir):
        # Calculate the relative path from the source directory
        relative_path = os.path.relpath(src_root, src_dir)
        # Calculate the destination directory path
        dst_root = dst_dir / relative_path

        # Ensure the destination directory exists
        os.makedirs(dst_root, exist_ok=True)

        for file in files:
            src_file = os.path.join(src_root, file)
            dst_file = os.path.join(dst_root, file)

            if should_copy(src_file, dst_file):
                print(f'Copying {src_file} to {dst_file}')
                shutil.copy2(src_file, dst_file)
            else:
                print(f'Skipping {src_file}, no changes detected.')

# Define the source and destination directories
source_directory = r'C:\Users\david\OneDrive\Masters'
destination_directory = r'H:\Masters'

# Synchronize the directories
sync_directories(source_directory, destination_directory)


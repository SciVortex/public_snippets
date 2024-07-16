# Mount Google Drive in Colab
import os

# Define the paths
gdrive_path = "/gdrive"
storage_path = "/gdrive/My Drive/colab/storage"
content_drive = "/content/drive"

# Create the directories
os.makedirs(gdrive_path, exist_ok=True)
os.makedirs(storage_path, exist_ok=True)

# Link the storage path to the content drive
if os.path.islink(content_drive):
    os.unlink(content_drive)
os.symlink(storage_path, content_drive)

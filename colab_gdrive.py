# Mount Google Drive in Colab
import os

# Define the paths
storage_path = "/gdrive/My Drive/colab/storage"
content_drive = "/content/drive"

from google.colab import drive
drive.mount('/gdrive')

os.makedirs(storage_path, exist_ok=True)

os.symlink(storage_path, content_drive)

def mount_google_drive(
    mountPoint = '/gdrive' ,
    drivePath = 'colab/storage', 
    localPath = '/content/drive'
  ):
  import os

  storage_path = f"{mountPoint}/My Drive/{drivePath}"

  from google.colab import drive
  drive.mount(mountPoint)
  os.makedirs(storage_path, exist_ok=True)
  os.symlink(storage_path, localPath)

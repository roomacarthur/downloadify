"""
Downloads Folder sorting script.

By = https://www.roomacarthur.dev
Repo = https://github.com/roomacarthur/downloadify

NOTE: please create a dummy file in downloads and copy some random files into it to test if unsure. 
"""

import os
import shutil

# file extensions for each category.
categories = {
    "Audio": ['.aif', '.cda', '.mid', '.midi', '.mp3', '.mpa', '.ogg', '.wav', '.wma'],
    "Compressed": ['.7z', '.deb', '.pkg', '.rar', '.rpm', '.tar.gz', '.z', '.zip'],
    'Code': ['.js', '.jsp', '.html', '.ipynb', '.py', '.java', '.css'],
    'Documents': ['.ppt', '.pptx', '.pdf', '.xls', '.xlsx', '.doc', '.docx', '.txt', '.tex', '.epub'],
    'Images': ['.bmp', '.gif', '.ico', '.jpeg', '.jpg', '.png', '.jfif', '.svg', '.tif', '.tiff'],
    'Softwares': ['.apk', '.bat', '.bin', '.exe', '.jar', '.msi', '.py'],
    'Videos': ['.3gp', '.avi', '.flv', '.h264', '.mkv', '.mov', '.mp4', '.mpg', '.mpeg', '.wmv'],
    'Others': []
}


"""
@@@@@ Downloads Folder @@@@@

Change this to math the path to your own downloads folder.

1. Open file explorer. 
2. right click on the downloads folder
3. Click "Copy as path"
4. Paste below in the r'Raw string' below.
"""

downloads_root = r"Your Downloads Folder Path"  # e.g. "C:\Users\Bob\Downloads"


# Create Sub Folders within Downloads Folder.

for category in categories:
    os.makedirs(os.path.join(downloads_root, category), exist_ok=True)


# Sort files.

for file in os.listdir(downloads_root):
    file_path = os.path.join(downloads_root, file)
    if os.path.isfile(file_path):
        ext = os.path.splitext(file)[1].lower()
        destination = 'Others'  # This is the default category

        for category, extensions in categories.items():
            if ext in extensions:
                destination = category
                break

        shutil.move(file_path, os.path.join(downloads_root, destination, file))

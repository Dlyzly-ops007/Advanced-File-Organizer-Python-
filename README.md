# Advanced-File-Organizer-Python-
A powerful and customizable file organizer that automatically sorts files into meaningful folders based on their type (Images, Music, Videos, Documents, Code, Archives, etc.).
This version includes:

Custom category mapping
Safe file moving (no overwriting)
Progress bar
Colored terminal output
Automatic folder creation
"Others" category for unknown file types
Clean and beginner-friendly structure

🚀 Features

✔ Organizes any folder with one command
✔ Custom categories (Music, Videos, Documents, Images…)
✔ Automatically groups files based on extension
✔ Creates folders if they don’t exist
✔ Prevents overwriting by adding _copy
✔ Fast and clean tqdm progress bar
✔ Color-coded output using colorama
✔ Supports ALL common extensions
✔ Unknown file types go into an Others folder

📦 Requirements

Only two external modules are used:
Install dependencies:
pip install tqdm colorama

Everything else uses Python’s standard library.

🛠 How to Use

Download / clone the repository
Place organizer.py anywhere
Run the script:
python organizer.py


When asked, enter the folder path you want to organize.
Example:

Enter folder path to organize: C:\Users\YourName\Downloads
The script will:
Scan all files
Detect their types
Create folders like:

Images/
Music/
Videos/
Documents/
Archives/
Code/
Others/

Move each file safely

📁 Category Mapping (Editable)

You can edit categories in the script:

CATEGORY_MAP = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Music": [".mp3", ".wav", ".flac"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx"],
    "Archives": [".zip", ".rar", ".7z"],
    "Code": [".py", ".cpp", ".js", ".html", ".css", ".java"],
}
Add or remove any file type you want — the script adjusts automatically!

🧠 How It Works

Script reads all files in the chosen directory
For each file:
Gets extension (.mp3, .pdf, etc.)
Matches it against CATEGORY_MAP
If extension found → moves to that folder
If not found → moves to Others
For safety:
If a file already exists in the destination folder, a copy is created:
file.pdf → file_copy.pdf

Shows progress with:
Green bar
Colored console output

📸 Example
Before:
song.mp3
image.png
notes.pdf
video.mp4
script.py
randomfile.xyz

After running the script:
Music/
   song.mp3
Images/
   image.png
Documents/
   notes.pdf
Videos/
   video.mp4
Code/
   script.py
Others/
   randomfile.xyz

🎯 Perfect For
Downloads folder cleanup
Desktop cleanup
Students, developers, office users
Automating messy directories

